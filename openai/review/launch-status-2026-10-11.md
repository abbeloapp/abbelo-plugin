# Launch status — October 11, 2026

## Scope and verified package

The owner authorized completing the public Abbelo plugin. Code and package builds were performed through GitHub cloud tools. The owner subsequently allowed a narrow exception to inspect the signed-in OpenAI and WorkOS settings in their browser. No local shell, deployment, production permission change, new consent grant, or paid session was used.

- Existing draft PR: https://github.com/abbeloapp/abbelo-plugin/pull/1
- Verified package commit: `7c9e0ac36c3cae00a30078614e8df3b963e4db35`
- Package validation/build: https://github.com/abbeloapp/abbelo-plugin/actions/runs/38204893232
- Candidate artifact: https://github.com/abbeloapp/abbelo-plugin/actions/runs/38204893232/artifacts/11726947433
- Inner ZIP SHA-256: `8a4a75fe8f0f1213e06c377ae9879419f2a8945fc1af3e01c307099e7d7a3e89`
- Six-file ZIP validation, compatibility manifest validation, reproducibility and integrity checks passed. The submission guard correctly remained false.
- Public-discovery consistency check failed because authorization-server metadata does not advertise the custom Abbelo scopes. This is not proof that a particular client cannot request them.
- Public discovery evidence: https://github.com/abbeloapp/abbelo-plugin/actions/runs/38204893232/artifacts/11727150990

Candidate 0.1.1 retains the existing white-backed Abbelo logo and updates saved links to `/chat?conversation=<id>`. App source at `83172d1e75c04bef6f3f293463b19d05813f41f5` routes `/chat` through HomeWorkspace, which handles the saved work-conversation ID. The root Cursor/Grok package is unchanged.

## OpenAI portal inspection

Observed October 11 Pacific / October 12 UTC:

- Public submission draft: `plugin_asdk_app_6abda5a4005081918646fb59fb8cc71c`.
- Existing draft version ID: `appsub_6abda5a400808191833c695930b5c6ab`.
- Publication: **Not published**. Review: **Not submitted**. MCP configuration: **Configuration incomplete**.
- Domain verification passed. MCP authorization is required. No tool findings are available.
- Server configuration remains streamable HTTP at `https://abbelo.com/mcp`, with empty custom headers and OAuth.
- The setup connection flow returned without completing authorization. The separate scan connection flow reported: **Could not confirm the connection. Refresh status before trying again.**
- No consent screen was approved. The full current authorization request, requested scope list and public-draft callback were not exposed in the inspected UI. Do not invent those details or equate the generic current failure with a verified new `invalid_scope` error.
- Browser tab metadata identifies the installed plugin separately as `plugin_asdk_app_6ac55feee6e4819180f38781a0773d54`. The owner's screenshot shows installed version 1.0.0. It must not be overwritten as though it were the public draft.
- The current read-only Abbelo connector returned `UNAUTHORIZED` and requested reauthentication.

## Production WorkOS inspection

Environment: `environment_01M32YFMPHV05ZNEQNFT31HNVQ`, Abbelo's Project, Production.

- Client ID Metadata Document registration: enabled.
- Dynamic Client Registration: disabled.
- Default MCP resource: `https://abbelo.com/mcp`.
- External sign-in URI: `https://abbelo.com/connect/mcp`.
- Both permissions exist in Authorization: `abbelo:read` and `abbelo:write`.
- Manual ChatGPT application `app_01M3JKJDVEPY8KRDHQNTA1X0Y3` has both custom scopes assigned.
- CIMD ChatGPT application `app_01M4BM3RMB00RP7ENQZMJYQGR5` has no editable scope section.
- Both inspected ChatGPT records use callback `https://chatgpt.com/connector/oauth/1y9f3YO8BNrS`; the CIMD client ID is `https://chatgpt.com/oauth/1y9f3YO8BNrS/client.json`. These records have not been matched to the public submission draft's current authorization request.
- Connect Configuration and Authorization Configuration did not expose environment-default custom-scope controls.
- WorkOS support's scope guidance describes CIMD defaults as support-managed and environment-wide. Account-specific diagnosis remains necessary; public metadata alone is insufficient.
- The first inspected support thread used a different email identity from the dashboard. After the owner authorized sending from the dashboard member mailbox, inspection of that mailbox revealed later correspondence. Provider support had already reported enabling a team-level Default scopes control on October 7; the control is still absent from the current production Connect Configuration page after reloading. Treat this as a provider/UI discrepancy, not proof that defaults are configured.
- The owner-authorized follow-up was sent on October 11 at 10:06 PM Pacific from the dashboard member mailbox to WorkOS support in the existing thread. Gmail sent-message search verified the new reply. It reports the missing control and asks for diagnosis and the exact scope proposal before changing production settings or grants. Private message bodies and mailbox identifiers are not copied into this public repository.
- No WorkOS configuration, client, permission, credential, grant or account was changed.

## Remaining work

1. Resolve the reported-but-missing Default scopes control with WorkOS, using the sent support follow-up. Obtain account-specific diagnosis including the exact rejected scope and proposed environment-default change. Explain the effect on existing/future clients, consents and refresh tokens before applying any change.
2. Capture the public draft's actual authorization request and callback, including advertised OIDC scopes. Do not reuse a different plugin's callback or infer enabled client scopes from discovery alone.
3. Preserve explicit local grants, account/client binding, PKCE, resource audience, expiry, revocation and Guide entitlements. Do not fix connection errors by weakening authorization.
4. Reconnect and prove read-only access first. Then complete the documented bounded session/rejection cases, same-conversation results, refresh and revocation.
5. Review the existing recording on `review-demo-2026-10-06` at `review-assets/abbelo-review-walkthrough.mp4`; it exists but was not validated in this pass. Preserve it.
6. Upload the verified package to the matched listing, supply the real reviewer fixture and demo, complete countries/commerce/publisher declarations and scans, and submit for OpenAI review. Publish after approval.

The package has not been uploaded, merged, submitted, approved or publicly published in this pass. No authenticated acceptance cases or paid requests were run. Unknown legal facts and unresolved access must not be marked as completed.

Sources: [OpenAI authentication](https://developers.openai.com/plugins/build/auth), [OpenAI submission](https://developers.openai.com/plugins/deploy/submission), [WorkOS scope configuration](https://workos.com/docs/authkit/connect/token-claims#configure-client-scopes).
