# Launch status — October 11, 2026

## Scope and evidence

The owner requested completion of the public Abbelo plugin and required cloud tools instead of controlling their computer. No local shell or browser is needed for the GitHub package build.

- Existing package PR: https://github.com/abbeloapp/abbelo-plugin/pull/1
- Public submission draft recorded in previous receipts: `plugin_asdk_app_6abda5a4005081918646fb59fb8cc71c`, package 0.1.0. Its current portal state has not been read in this pass.
- The owner's screenshot shows an installed 1.0.0 plugin with a generic icon. Its identity has not been matched to the public draft. Do not overwrite a different listing or downgrade its version.
- Read-only `abbelo_get_connection` returned `UNAUTHORIZED` and requested reauthentication. This does not establish the cause of the earlier public-draft OAuth failure.
- The separate connection investigation reports an October 8 WorkOS support reply about `invalid_scope` before consent, production CIMD enabled and environment-level scope defaults. This is contextual evidence, not a fresh provider configuration read. Exact rejected scopes and their impact remain unverified here.
- No authenticated acceptance cases or paid session requests were run in this pass.
- A recording exists on `review-demo-2026-10-06` at `review-assets/abbelo-review-walkthrough.mp4`. Its contents and reviewer suitability were not verified in this pass. Preserve it.
- GitHub and service connectors are available. No connected cloud tool exposes WorkOS Connect administration or OpenAI plugin draft upload/submission.

## Prepared package

Candidate 0.1.1 retains the existing white-backed Abbelo logo and updates saved links to `/chat?conversation=<id>`. The app source at `83172d1e75c04bef6f3f293463b19d05813f41f5` routes `/chat` through HomeWorkspace, which handles the saved work-conversation ID. The legacy `/home` route is retained by the app, not removed by this package.

The GitHub workflow builds a reproducible six-file ZIP and keeps package validation separate from submission readiness. Public discovery checks inspect only fixed HTTPS metadata URLs and the unauthenticated MCP challenge. They cannot prove client scope entitlement, consent, refresh, private tool access, or OpenAI approval.

## Next required connection evidence

1. Match the exact plugin ID and draft version, then inspect its current MCP connection error.
2. Capture the actual authorization request's issuer, client metadata URL/client ID, redirect URI and requested scope names. Keep tokens, authorization codes, state values and PKCE material out of source and support notes.
3. In the matching WorkOS environment, verify which requested scopes the specific registration mode permits. OpenAI requests advertised OIDC scopes by default, so checking only `abbelo:read` and `abbelo:write` is insufficient. Do not infer enabled client scopes from discovery alone.
4. Prepare any necessary environment-wide scope change with its precise impact before applying it. Preserve Abbelo's explicit local grants, account/client binding, PKCE, resource audience checks and revocation.
5. Reconnect and prove read-only access first. Then complete the documented bounded session and rejection cases, same-conversation results, refresh and revocation.

Never fix `invalid_scope` by disabling authorization, widening local grants, advertising false issuer capabilities or reusing an unrelated callback.

## Final portal work

After connection and acceptance pass, upload the verified package to the matched existing listing, review the recording, supply the real demo URL and reviewer fixture, complete countries/commerce/publisher declarations and scans, submit for review, then publish after OpenAI approval. The owner has authorized finishing the public launch. Unknown legal facts and missing admin access remain factual blockers, not a reason to invent a declaration.

Sources: [OpenAI authentication](https://developers.openai.com/plugins/build/auth), [OpenAI submission](https://developers.openai.com/plugins/deploy/submission), [WorkOS MCP](https://workos.com/docs/authkit/mcp).
