# Launch status — October 11–12, 2026

## October 12, 15:19 UTC — OpenAI support escalation confirmed

The owner explicitly approved sending the prepared diagnostic report to OpenAI Support using the Abbelo account email. The report was sent through the official Help Center support chat and verified in its visible transcript. A follow-up clarified that this is the **public Apps/Plugins submission portal**, preserved separately consented session tools, and requested a human specialist's account-specific remediation proposal before registration/grant changes.

The initial AI support response gave generic recreation and scope advice, without inspecting the registration. That is **not** an authoritative reset procedure or permission to delete/recreate the plugin, change domain verification, broaden defaults, or relabel write tools. After clarification, the owner-authorized escalation was confirmed by the visible status **Escalation requested** and a message saying the case was escalated to a support specialist, with replies also sent by email. No case number was exposed. No human diagnosis or fix is available yet.

The approved original report remains preserved in `openai-oauth-support-draft-2026-10-12.md` as a historical draft; its earlier “not sent” header describes its state at preparation, superseded by this receipt. Do not resend or create a duplicate ticket. No raw HAR, token, cookie, secret or OAuth state was transmitted.

Continue with the specialist's supported remediation once available, then verify the outgoing client/scope request before authorization. The public plugin is still unsubmitted/unpublished; authenticated discovery, acceptance, reviewer setup and remaining review gates are pending. No production configuration, permission, credential, paid request, deployment or merge changed during this escalation.

## October 12, 15:06 UTC — runtime client mismatch confirmed

This receipt supersedes earlier uncertainty about the runtime client and requested scope set. The exact rejected individual scope remains unknown.

OpenAI's visible Connect network response for runtime version `asdk_app_v_41691e2e6364819186d6356da7cee0cd` returns an authorization URL using the **old CIMD client** `https://chatgpt.com/oauth/1y9f3YO8BNrS/client.json` with **openid email offline_access abbelo:read abbelo:write**. Its resource is `https://abbelo.com/mcp` and callback is `https://chatgpt.com/connector/oauth/1y9f3YO8BNrS`.

This differs from the saved 0.1.2 settings: **provided** client `client_01M3JKJDVEWD5X2B368JK6XZ3Q`, authentication method **none**, initial scopes **abbelo:read**. The manual client is not the client used by this observed request; do not diagnose the manual client's scope permissions from this failure.

- Evidence: [sanitized request comparison](oauth-runtime-mismatch-2026-10-12.json). The response was read through Chrome's visible Network UI, not hidden browser state or a private API call. State, nonce, challenge values, credentials and tokens are omitted.
- The inspected Connect attempt was canceled before Continue or authorization. It establishes the outgoing request configuration, not a new provider rejection. The earlier 14:36:36 UTC callback remains the verified `invalid_scope` receipt.
- The portal still shows **Not published**, **Not submitted**, **Configuration incomplete**, **Authorization required**, and no discovered tool findings.
- The inspected MCP selector has only `abbelo`; the plugin menu offers Download draft ZIP and Delete plugin. No supported registration reset control was found. Do not delete the plugin, replace the domain challenge, broaden WorkOS defaults or weaken API scope checks as a workaround.
- OpenAI documents that existing client registration can lock credential changes after upload. This is consistent with the observed mismatch; the internal mechanism remains unverified.
- No new support message, permission/credential change, paid request, production deployment or merge occurred.

Next: ask OpenAI for the supported way to reset/rebind this existing draft's MCP OAuth registration to the saved provided client, preserving plugin identity and domain verification. A support report is prepared in [openai-oauth-support-draft-2026-10-12.md](openai-oauth-support-draft-2026-10-12.md); it has **not been sent**. Obtain owner authorization for that new recipient. After a supported fix, verify the actual outbound client/scopes before sign-in; complete authenticated tool discovery, acceptance cases, reviewer setup and submission gates. Do not rebuild/reupload the unchanged package or repeat failed authorizations without a relevant state change.

Sources: [OpenAI saved-registration limitation](https://developers.openai.com/plugins/deploy/submission#configure-authentication-for-submission), [OpenAI troubleshooting escalation](https://developers.openai.com/plugins/deploy/troubleshooting#when-to-escalate).

## October 12 continuation — 0.1.2 uploaded; current invalid_scope captured

The owner explicitly asked the agent to open Chrome and finish the upload. The public draft now contains **0.1.2**. This supersedes the earlier notes that the package was not uploaded.

### Verified actions and results

- The GitHub Actions browser artifact URL still hit `ERR_BLOCKED_BY_CLIENT`. No browser security setting or warning was bypassed. A dedicated GitHub `download_workflow_artifact` connector retrieved artifact `11727479303`; its returned file was downloaded through the supported browser download event and uploaded through the OpenAI file chooser.
- Uploaded candidate: commit `07408386dd551470ced4badae0f7258deb19b552`, direct portal artifact digest `sha256:0e1872dcdbabf62f4f2509b36f448b2c3ebdadef356dbcfa62ce51299297bb49`. No local shell or package build ran.
- Existing public draft: `plugin_asdk_app_6abda5a4005081918646fb59fb8cc71c`; draft version ID `appsub_6abda5a400808191833c695930b5c6ab`.
- Portal displays **Metadata & skills version 0.1.2 · Draft**, metadata **No findings**, and skill **Checks passed**.
- MCP saved settings visibly contain `client.mode: provided`, `clientId: client_01M3JKJDVEWD5X2B368JK6XZ3Q`, `tokenEndpointAuthMethod: none`, and `defaultScopes: [abbelo:read]`. Domain remains verified.
- One Connect/Continue attempt returned without authorization. A focused browser-history lookup captured the actual callback at **2026-10-12 14:36:36 UTC / 07:36:36 Pacific**: `https://chatgpt.com/connector/oauth/1y9f3YO8BNrS?error=invalid_scope` (OAuth state omitted). It relayed to the OpenAI platform at 14:36:38 UTC.
- This proves a **current invalid_scope response** and matches the public draft flow's callback to the WorkOS manual client. It does **not** expose the full outbound authorization request, actual runtime client ID, or rejected scope. Saved package settings alone do not prove an older client registration was replaced.
- Production WorkOS manual ChatGPT client still has `abbelo:read` and `abbelo:write`, and the exact matching callback. No changes were made.
- WorkOS Connect Configuration and its Manage dialog still expose CIMD enabled, DCR disabled, the MCP resource and external sign-in URI; **no Default scopes control**. The Events page has no event for this failed attempt; it does not provide the missing authorization-request diagnosis.
- Portal reviewer setup offers username/password or a dedicated magic-link/email-code reviewer account. No reviewer account, grant, country setting, legal declaration or credential was created/saved. Do not use a real production account as the reviewer fixture.
- Status remains **Not published**, **Not submitted**, **Configuration incomplete**, **Authorization required**, and no discovered tool findings. Metadata/skill success is not MCP scan success.
- No new support email, WorkOS mutation, consent grant, paid request, merge or production deployment occurred.

### Continue from here

Do not rebuild or reupload 0.1.2 merely because older notes say it is absent. Obtain the failed authorization request's runtime client ID and exact rejected scopes from the provider/OpenAI diagnostics or account-specific support. Resolve any saved-registration mismatch through a supported flow; do not delete clients, relax API checks or broaden environment defaults speculatively. Once authorization is fixed, complete authenticated acceptance, the dedicated reviewer fixture, review materials/declarations and MCP scans, then submit and publish after approval. The previous cloud public-discovery failure remains unresolved and must not be bypassed.

## Latest continuation — registered-client candidate

The owner asked to continue on October 11. A new WorkOS reply at 10:08 PM Pacific gives no verified rejected scope, no live configuration diagnosis and no cause for the missing Default scopes control. Production Connect Configuration was inspected again: the control is still absent. No further support message was sent.

OpenAI's current packaging documentation explicitly supports selecting an existing registered client in `mcp.json`. Candidate **0.1.2** now prepares that route:

- Commit: `07408386dd551470ced4badae0f7258deb19b552`.
- Existing manual ChatGPT client: `client_01M3JKJDVEWD5X2B368JK6XZ3Q`, public client / PKCE, `tokenEndpointAuthMethod: none`.
- Initial `defaultScopes: ["abbelo:read"]`; provider OIDC discovery and explicit Abbelo Session consent remain in place.
- The existing callback `https://chatgpt.com/connector/oauth/1y9f3YO8BNrS` remains **unmatched to the public draft**. Do not authorize against a guessed callback or overwrite the existing one.
- This is prepared source only. No WorkOS settings, credentials, grants, production deployment or saved OpenAI registration changed.
- Cloud package job and five negative OAuth-configuration cases passed: https://github.com/abbeloapp/abbelo-plugin/actions/runs/38207433424/job/114673929374
- Deterministic inner ZIP SHA-256: `c1bef55c031351ce60b589ee0e961c63684a90ff4b39773c1ea788593b2213c4`.
- Direct-upload artifact with exactly the six validated plugin files, including hidden compatibility metadata: https://github.com/abbeloapp/abbelo-plugin/actions/runs/38207433424/artifacts/11727479303
- Portal artifact digest: `sha256:0e1872dcdbabf62f4f2509b36f448b2c3ebdadef356dbcfa62ce51299297bb49`.
- The separate public-discovery job still fails. No check was bypassed, and the PR remains unmerged.
- Chrome blocked the artifact download host `productionresultssa6.blob.core.windows.net` with `ERR_BLOCKED_BY_CLIENT`. The browser download operation returned no file path. No package was uploaded. Do not claim the draft has the new client configuration.
- The existing public draft's **Reupload draft** dialog is open for handoff. It accepts a ZIP file, not an artifact URL.

Next: get the verified portal artifact into the existing public draft, inspect the saved auth settings and exact callback, and resolve any client-registration lock before authorization. A callback change or new consent needs the appropriate concrete approval; do not reset security state as a shortcut. If provided-client registration is unavailable for this existing connection, preserve it and await WorkOS's account-specific fix. Existing acceptance, reviewer, recording, declarations, scan and publication gates below remain open.

Sources: [OpenAI MCP auth packaging](https://developers.openai.com/plugins/build/plugins#configure-mcp-authentication), [OpenAI submission configuration](https://developers.openai.com/plugins/deploy/submission#configure-authentication-for-submission), [WorkOS scopes](https://workos.com/docs/authkit/connect/token-claims#configure-client-scopes).

## Previous scope and verified package

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
