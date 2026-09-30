# Abbelo for OpenAI: submission candidate

Prepared September 30, 2026. **Not submitted, approved, published, or verified in ChatGPT/dots.** The candidate is a separate package. The repository’s root Cursor manifest, MCP configuration, workflow skill and logo remain unchanged.

## What is included

- `abbelo/plugin.json`: portable Agent Plugins 1.0.0 manifest, OpenAI listing and exactly five positive/three negative review cases.
- `abbelo/mcp.json`: the existing `https://abbelo.com/mcp` endpoint using Streamable HTTP. No Cursor variable, app reference, hooks, local command, credential or authorization header.
- `abbelo/skills/abbelo/SKILL.md`: adapted existing workflow, explicit permissions and credit approval, same-conversation results, exact retries and account/Guide boundaries.
- `abbelo/assets/abbelo.png`: byte-identical existing Abbelo artwork.
- `abbelo/.codex-plugin/plugin.json`: derived compatibility metadata for older Codex loaders. The portable root and inline `extensions.com.openai` are authoritative in the current public importer. Compatibility metadata omits the newer support field; the authoritative listing includes it. The builder checks drift.
- `review/`: operator-only preparation documents and unresolved gates, excluded from the distributable ZIP. Never put reviewer credentials here.

Abbelo is the existing product/author name, not a claim that its legal publishing identity has been verified. `developerName` must match the identity selected in the portal. Country targeting and commerce declarations remain omitted until the owner confirms them. No fabricated demo URL is present.

## Rebuild and validate

Use Python 3.9 or later and a virtual environment outside this repository:

```sh
python3 -m venv /tmp/abbelo-plugin-validation
/tmp/abbelo-plugin-validation/bin/pip install -r openai/requirements.txt
/tmp/abbelo-plugin-validation/bin/python scripts/build-openai.py --output /tmp/abbelo-openai-candidate.zip
/tmp/abbelo-plugin-validation/bin/python scripts/build-openai.py --require-submission-ready
```

The final command intentionally fails until every release gate has real evidence. It does not submit anything. Default validation proves local schema, listing limits, image dimensions, tool names, case counts, included-file allowlist, compatibility consistency, absence of credential/config placeholders, and archive integrity. It does not replace the portal’s automated scans or live host tests. Repeated builds with the same files produce identical ZIP bytes.

Vendored schemas are exact public Agent Plugins 1.0.0 schema files downloaded on September 30, 2026 from the `$id` in each file. Schema provenance and OpenAI requirements are in [requirements](review/requirements.md).

## Required next steps

1. Confirm the legal publisher, country, availability, support/policies and existing-account payment model.
2. Review the companion Abbelo source changes for explicit session permission and OpenAI OAuth error metadata. Obtain approval before deployment.
3. Follow [OAuth setup](review/oauth.md). Capture the exact callback from the portal and obtain approval before registering an OpenAI client. Preserve existing clients, scopes and revocation rules.
4. Obtain a synthetic reviewer account and an explicit paid-test budget. Run [acceptance](review/acceptance.md), including the packaged review cases, in actual ChatGPT and a dot.
5. Record [the demo](review/demo.md); add the reviewed accessible URL to the manifest.
6. Complete portal checks, then request approval to submit. Approval by OpenAI is a separate event. Publication needs another owner decision.
