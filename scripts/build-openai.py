#!/usr/bin/env python3
"""Validate and deterministically package the separate OpenAI candidate. No network."""
import argparse
import hashlib
import json
import re
import struct
import zipfile
from pathlib import Path
from urllib.parse import urlparse

import jsonschema
import yaml

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'openai/abbelo'
FILES = ['.codex-plugin/plugin.json', 'LICENSE', 'assets/abbelo.png', 'mcp.json', 'plugin.json', 'skills/abbelo/SKILL.md']
TOOLS = {'abbelo_get_connection','abbelo_find_work','abbelo_start_conversation','abbelo_continue_session','abbelo_get_run','abbelo_get_conversation'}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def validate():
    actual = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file())
    require(actual == sorted(FILES), 'Unexpected or missing package files')
    for relative in FILES:
        path = ROOT / relative
        require(not path.is_symlink(), 'Symlinks are not permitted')
        require(ROOT in path.resolve().parents, 'Path must stay inside package')
    manifest = json.loads((ROOT/'plugin.json').read_text())
    mcp = json.loads((ROOT/'mcp.json').read_text())
    for kind, value in [('plugin',manifest),('mcp',mcp)]:
        schema = json.loads((REPO/f'openai/schemas/{kind}.schema.json').read_text())
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(value)
    require(mcp['mcpServers'] == {'abbelo':{'type':'streamable-http','url':'https://abbelo.com/mcp'}}, 'One remote endpoint; no variables, headers, auth secrets or commands')
    require(re.fullmatch(r'\d+\.\d+\.\d+',manifest['version']), 'Version must be a release semver')
    extension = manifest['extensions']['com.openai']
    require(set(extension) <= {'interface','review','publication'}, 'Unexpected OpenAI extension')
    interface = extension['interface']
    for key, limit in [('displayName',30),('shortDescription',30),('longDescription',4000),('developerName',80)]:
        require(isinstance(interface[key],str) and 0 < len(interface[key]) <= limit, f'Invalid listing {key}')
    for key in ['websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL']:
        url = urlparse(interface[key])
        require(url.scheme == 'https' and url.netloc == 'abbelo.com' and not url.username and len(interface[key]) <= 1024, f'Invalid URL {key}')
    require(interface['category']=='Productivity', 'Recheck category against portal before changing it')
    require(0 < len(interface['defaultPrompt']) <= 3 and all(0<len(p)<=128 for p in interface['defaultPrompt']), 'Invalid starter prompts')
    require(len(interface['capabilities'])<=20 and all(0<len(c)<=120 for c in interface['capabilities']), 'Invalid capabilities')
    require(interface['logo']==interface['composerIcon']=='./assets/abbelo.png','Reuse existing branding')
    image=(ROOT/'assets/abbelo.png').read_bytes()
    require(image == (REPO/'assets/abbelo.png').read_bytes(), 'Branding differs from existing package')
    require(image[:8]==b'\x89PNG\r\n\x1a\n' and len(image)<=5*1024*1024,'Invalid image')
    width,height=struct.unpack('>II',image[16:24])
    require(48 <= width == height <= 4096,'Icon dimensions must be square, 48–4096')
    cases=extension['review']['test_cases']
    require(set(cases)=={'positive','negative'},'Invalid test groups')
    for group,count in [('positive',5),('negative',3)]:
        require(len(cases[group])==count,f'Exactly {count} {group} cases required')
        for case in cases[group]:
            require(set(case)=={'description','prompt','tools_triggered','expected_behavior'},'Invalid case fields')
            require(all(isinstance(v,str) and v.strip() for v in case.values()),'Empty case value')
            names=set(case['tools_triggered'].split(', '))
            require(names <= TOOLS or (group=='negative' and names=={'None'}),'Unknown tool in review case')
    source=(ROOT/'skills/abbelo/SKILL.md').read_text()
    frontmatter=yaml.safe_load(source.split('---',2)[1])
    require(frontmatter['name']=='abbelo' and frontmatter['description'],'Invalid skill metadata')
    require(all(name in source for name in TOOLS),'Skill must cover all existing tools')
    for relative in FILES:
        if relative.endswith(('.json','.md')):
            content=(ROOT/relative).read_text()
            require(not re.search(r'\$\{|\[TODO:|sk-[A-Za-z0-9]|Bearer [A-Za-z0-9._-]{15,}|test_credentials|reviewer_instructions',content),'Possible placeholder, credential or unsupported review field')
    compat={k:v for k,v in manifest.items() if k not in ['$schema','extensions']}
    compat.update(skills='./skills/',mcpServers={'abbelo':{'type':'http','url':'https://abbelo.com/mcp'}},interface={k:v for k,v in interface.items() if k!='supportURL'})
    require(json.loads((ROOT/'.codex-plugin/plugin.json').read_text()) == compat,'Compatibility manifest drift: derive it from portable metadata')
    return manifest

def submission_blockers(manifest):
    readiness=json.loads((REPO/'openai/review/readiness.json').read_text())
    blocked=[key for key,value in readiness['gates'].items() if value is not True]
    ext=manifest['extensions']['com.openai']
    if not ext.get('review',{}).get('demo_recording_url'): blocked.append('recorded_demo_url_in_package')
    if 'countries' not in ext.get('publication',{}): blocked.append('country_allowlist_in_package')
    if 'commerce' not in ext.get('review',{}): blocked.append('commerce_declaration_in_package')
    return blocked

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--require-submission-ready',action='store_true')
    args=parser.parse_args()
    manifest=validate()
    blockers=submission_blockers(manifest)
    if args.require_submission_ready:
        require(not blockers,'Submission blocked: '+', '.join(blockers))
    report={'packageValidation':'passed','submissionReady':not blockers,'blockers':blockers}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(args.output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
            for relative in sorted(FILES):
                info=zipfile.ZipInfo(relative,date_time=(2026,9,30,0,0,0))
                info.create_system=3
                info.external_attr=0o100644<<16
                info.compress_type=zipfile.ZIP_DEFLATED
                archive.writestr(info,(ROOT/relative).read_bytes(),compresslevel=9)
        with zipfile.ZipFile(args.output) as archive:
            require(archive.testzip() is None and archive.namelist()==sorted(FILES),'Archive integrity failed')
        report.update(zip=str(args.output),sha256=hashlib.sha256(args.output.read_bytes()).hexdigest())
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    main()
