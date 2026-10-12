#!/usr/bin/env python3
"""Read only public OAuth metadata. No login, grants, tokens or AI requests."""
import json
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener

RESOURCE = 'https://abbelo.com/mcp'
METADATA = 'https://abbelo.com/.well-known/oauth-protected-resource/mcp'
ISSUER = 'https://satisfying-gust-31.authkit.app'

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = build_opener(NoRedirect())
report = {
    'checkedAt': datetime.now(timezone.utc).isoformat(),
    'checks': {},
    'limitations': [
        'Discovery does not prove requested scopes are enabled for the actual OAuth client.',
        'No authenticated tool, consent, refresh, revocation, paid session or portal scan was tested.',
    ],
}
failures = []

def check(name, condition):
    report['checks'][name] = bool(condition)
    if not condition:
        failures.append(name)

def read(url, accept='application/json'):
    request = Request(url, headers={'Accept': accept, 'User-Agent': 'Abbelo-Plugin-Readiness/1.0'})
    try:
        response = opener.open(request, timeout=20)
    except HTTPError as error:
        response = error
    with response:
        body = response.read(131073)
        if len(body) > 131072:
            raise ValueError('Public metadata exceeded size limit')
        return response.status, response.headers, body

def run():
    status, _, body = read(METADATA)
    check('resource_metadata_http_200', status == 200)
    if status != 200:
        return
    resource = json.loads(body)
    report['resource'] = {key: resource.get(key) for key in ['resource', 'authorization_servers', 'scopes_supported', 'bearer_methods_supported']}
    check('exact_resource', resource.get('resource') == RESOURCE)
    check('expected_issuer', resource.get('authorization_servers') == [ISSUER])
    check('resource_read_scope', 'abbelo:read' in resource.get('scopes_supported', []))
    check('resource_write_scope', 'abbelo:write' in resource.get('scopes_supported', []))

    status, _, body = read(ISSUER + '/.well-known/oauth-authorization-server')
    check('authorization_metadata_http_200', status == 200)
    if status == 200:
        auth = json.loads(body)
        fields = ['issuer', 'authorization_endpoint', 'token_endpoint', 'scopes_supported',
                  'code_challenge_methods_supported', 'token_endpoint_auth_methods_supported',
                  'client_id_metadata_document_supported', 'registration_endpoint',
                  'authorization_response_iss_parameter_supported']
        report['authorizationServer'] = {key: auth.get(key) for key in fields}
        check('exact_issuer', auth.get('issuer') == ISSUER)
        check('pkce_s256', 'S256' in auth.get('code_challenge_methods_supported', []))
        for key in ['authorization_endpoint', 'token_endpoint']:
            check(key + '_https', str(auth.get(key, '')).startswith(ISSUER + '/'))
        check('authorization_read_scope', 'abbelo:read' in auth.get('scopes_supported', []))
        check('authorization_write_scope', 'abbelo:write' in auth.get('scopes_supported', []))

    status, headers, _ = read(RESOURCE, 'application/json, text/event-stream')
    challenge = headers.get('WWW-Authenticate', '')
    report['unauthenticatedMcp'] = {'status': status, 'challenge': challenge}
    check('unauthenticated_mcp_denied', status == 401)
    check('resource_challenge_present', 'resource_metadata="' + METADATA + '"' in challenge)

try:
    run()
except (URLError, ValueError, OSError) as error:
    # These requests contain no credentials or private user data.
    report['error'] = type(error).__name__ + ': ' + str(error)
    failures.append('public_discovery_unavailable')
report['passed'] = not failures
report['failures'] = failures
print(json.dumps(report, indent=2))
sys.exit(1 if failures else 0)
