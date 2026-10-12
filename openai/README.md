# Abbelo for OpenAI: submission candidate

Candidate **0.1.1**, updated October 11, 2026. Public submission, approval and publication are not verified. The root Cursor/Grok package is separate and unchanged.

## Package

The portable `abbelo/plugin.json` includes the OpenAI listing, correct Abbelo logo, starter prompts, and five positive/three negative review cases. `abbelo/mcp.json` connects to `https://abbelo.com/mcp`. The skill uses account permissions, approved session messages, exact request retries, and saved conversation links.

The compatibility manifest at `abbelo/.codex-plugin/plugin.json` is derived from the portable manifest. Review documents, readiness records and credentials are excluded from the six-file ZIP.

The screenshot supplied October 11 shows an installed **1.0.0** plugin with a generic icon and older read-only description. The known public submission draft is **0.1.0**. Match the plugin identifier in the portal before uploading this candidate; do not assume the installed plugin and public draft are the same listing. If updating an existing 1.0.0 lineage, first choose a newer version and regenerate both manifests.

## Build in GitHub

The [OpenAI package workflow](../.github/workflows/openai-package.yml) validates the package, builds it twice, compares the ZIP bytes, and uploads the ZIP, SHA-256 and readiness report as one artifact. A separate job reads public OAuth discovery without signing in or sending AI requests.

Download the artifact for the exact reviewed commit. Only `abbelo-openai-candidate.zip` goes to the OpenAI plugin portal. A green package build does **not** mean authentication works, acceptance passed, or the plugin is approved.

The release guard refuses a submission-ready result while evidence is missing. Existing historical receipts are preserved in `review/verification.json`; the latest handoff is [launch status](review/launch-status-2026-10-11.md).

For an independent rebuild with Python 3.9 or newer:

```sh
python -m pip install -r openai/requirements.txt
python scripts/build-openai.py --output /tmp/abbelo-openai-candidate.zip
python scripts/build-openai.py --require-submission-ready
```

The last command must fail until every recorded gate has evidence. It never submits anything.

## Remaining launch work

1. Match the installed plugin to the intended existing public draft and finish its OAuth connection. See [OAuth](review/oauth.md) and the latest launch status.
2. Run [acceptance](review/acceptance.md) with a dedicated reviewer account, including read/write separation, saved-session continuity, exact retries and revocation.
3. Review the existing recording before deciding whether it needs replacing; add the verified accessible demo URL.
4. Complete the actual portal scans, supported countries, commerce facts and required publisher declarations.
5. Submit the completed package for OpenAI review, then publish after approval. The owner's request to finish and go live authorizes this sequence; do not ask again for generic submission/publication permission. Missing factual declarations still require the owner's answers.

Schema provenance is in [requirements](review/requirements.md). This package does not change production authentication, existing provider clients or billing.
