# OAuth setup: pending exact dashboard values and approval

Do not use a sample callback or a Cursor client ID. Production authentication changes, including DCR/CIMD, require the owner's specific approval. Do not share an owner's token or put secrets in the ZIP.

## October 6 recheck and approved staging change

The live OpenAI draft still shows **Not submitted**, **Not published**, **Domain verified**, and **Authentication unavailable**. A fresh MCP rescan failed without discovering tools. The connection drawer exposes the MCP URL and a disabled OAuth selector, but no predefined client ID, secret, callback or CIMD document fields. The plugin actions menu offers only download and delete. Although OpenAI documents predefined clients, this draft's visible management surface does not expose that route. Do not substitute the personal developer-mode connection's client or callback.

Public discovery remains healthy: `/mcp` returns a 401 challenge pointing to the working protected-resource document, its issuer matches the authorization-server metadata, and that metadata advertises S256. Neither CIMD nor DCR is advertised. The root protected-resource URL returns 404, which is not by itself a defect because the 401 explicitly advertises the working `/mcp` metadata path. The provider's OIDC document omits PKCE methods; its OAuth authorization-server document includes S256.

Test the CIMD hypothesis in an isolated environment before proposing a production change. [WorkOS environments](https://workos.com/docs/authkit/environments) documents separate staging and production keys, users, and connections; staging supports localhost callbacks. After inspecting the current signed-in dashboard, the owner specifically approved **CIMD only in the existing staging environment**. That setting is now enabled; DCR remains disabled, with the already-correct sandbox resource and external sign-in URI unchanged. Public discovery confirms CIMD support. No documented CIMD client/domain allowlist was found, and the local emulator does not document CIMD coverage or prove real OAuth behavior. See [WorkOS testing](https://workos.com/docs/authkit/testing).

If staging proves compatibility, a later production proposal can enable **Client ID Metadata Document (CIMD) only** in **WorkOS → Abbelo Production → Connect → Configuration**, then reread public discovery and retry the OpenAI connection. Keep DCR off, the exact resource/audience `https://abbelo.com/mcp`, PKCE S256, current scopes, explicit user consent, and every existing grant/client/owner check. Do not add resource wildcards, a default resource, broad scopes, a guessed callback or a client secret. Production changes need their own approval.

CIMD changes client identification for the WorkOS environment; it must not be described as an OpenAI-only allowlist. The toggle permits additional clients to identify themselves and request consent. It does not itself authorize any member's saved work. Start subsequent testing with an approved synthetic reviewer identity and `abbelo:read`. Request `abbelo:write` only through a separately approved session-consent test. The provider also advertises `openid`, `email`, `profile`, and `offline_access`; inspect the actual requested identity and refresh scopes before completing consent.

The current adapter's encoded HTTPS client-ID handling passes synthetic tests, but real CIMD application metadata and token claims remain unverified. Grant activation requires exact client identity, PKCE and an adequate scope ceiling. Preserve those checks if the provider shape differs; diagnose the difference before proposing code changes. Current GitHub `main` confirms no initial client allowlist and still sends `user_consent_options` on every standalone completion. A first-party client therefore remains a separate compatibility risk; never remove the grant claim to bypass that rejection.

WorkOS sign-in is now resolved: a fresh dedicated tab confirmed the signed-in Abbelo project and its staging environment. Earlier automatic approval review rejected Google sign-in and a retry with parent-relayed authorization; those historical failures are not a current sign-in blocker. The approved staging CIMD setting is the only authentication change. No credential, OAuth grant, paid test, production setting or deployment changed. The older recovery attempt is not a reason to replay an identity mutation or assume a delayed write exists.

See `verification.json` → `lastRecheck` for public endpoint results and local validation provenance. The rebuilt package is byte-identical to the uploaded candidate; all eight MCP fixture scripts pass, but neither result is real ChatGPT/dot acceptance.

## Current staging configuration and next test

The authenticated WorkOS dashboard shows **Abbelo's Project → Staging**, environment `environment_01M32YFM32Z2Q6A7CA1EP88EC2`:

- CIMD: Enabled after the owner's specific approval. DCR: Disabled. The shared Enable control opened separate checkboxes; only CIMD was selected and saved.
- Resource indicator: `https://abbelo-git-codex-creator-payments-sandbox-abbeloapp.vercel.app/mcp`, already marked Default.
- External Sign-in URI: `https://abbelo-git-codex-creator-payments-sandbox-abbeloapp.vercel.app/connect/mcp`.
- Public issuer: `https://sympathetic-unknown-40-staging.authkit.app`; OAuth metadata now advertises `client_id_metadata_document_supported: true`, S256 and `none` client authentication. No DCR registration endpoint is advertised. Production metadata remains unchanged, without CIMD/DCR.
- Existing manual OAuth application **Abbelo MCP staging test**, client `client_01M3648H7JYA4EE2W23VDSW9K5`, has callback `http://127.0.0.1:8894/callback` and scope ceiling `abbelo:read`, `abbelo:write`. Its visible details expose no first-party or PKCE setting. A predefined-client test is not CIMD proof.

The saved change preserves the existing resource indicator, Default status, external sign-in URI, callbacks, scope ceiling, manual client and production environment. CIMD is environment-wide client identification, not an OpenAI-only restriction and not consent to read account data. Separate approval is needed for a synthetic read-only grant and any requested refresh scope.

Current Vercel project configuration confirms that sandbox-branch `SUPABASE_URL` and `NEXT_PUBLIC_ABBELO_SUPABASE_URL` both point to the separate Supabase preview project `nukwomvclaxavdmxzbvs`; production uses `apjgcwapxprihicahytd`. A separate sandbox-scoped Secret service-key entry exists; its value was not read. The current public browser bundle independently matches the sandbox project. Supabase's authenticated dashboard confirms the distinct Preview branch. No user rows or key values were read.

The active sandbox deployment `87G9inzEu72mHtzZnLUWKXUJoeow` still runs commit `3ad211e4a8551424207120d7f1a44b44bb1cc73b` from September 23. Exact-source comparison confirms URL-valued CIMD identifiers, PKCE, sole audience, `sid`, grant/client binding and scope intersection are present. A schema-only SELECT verified `mcp_grants.expires_at` is NOT NULL with a 30-day default, matching that older adapter. This can support an initial CIMD smoke test, but cannot establish current production consent text, diagnostics or until-disconnect connection lifecycle. The sandbox overview reports Unhealthy while the metadata query succeeds; its unhealthy component is not yet identified. Verify an approved synthetic identity and actual host CIMD metadata/callback before separate consent. No live token test has run.

## Verified endpoints

- Resource and MCP URL: `https://abbelo.com/mcp`
- Resource metadata: `https://abbelo.com/.well-known/oauth-protected-resource/mcp`
- Issuer: `https://satisfying-gust-31.authkit.app`
- Authorization: `https://satisfying-gust-31.authkit.app/oauth2/authorize`
- Token: `https://satisfying-gust-31.authkit.app/oauth2/token`
- PKCE: S256
- Existing connection scopes: `abbelo:read`, and explicitly approved `abbelo:write`
- Provider metadata also advertises `openid`, `email`, `profile`, `offline_access`. OpenAI may request advertised identity scopes by default; configure and test the dedicated client accordingly. Identity scopes never confer Abbelo resource access.

## Exact callback rule

OpenAI documents two patterns. With correctly implemented RFC 9207 issuer identification the stable callback is `https://chatgpt.com/connector_platform_oauth_redirect`. Otherwise the dashboard assigns `https://chatgpt.com/connector/oauth/{callback_id}`. These are documented patterns, **not approved registration values**.

Abbelo’s live issuer does not advertise `authorization_response_iss_parameter_supported`. Therefore do not choose the stable URL. The exact callback remains unknown until the MCP management form shows it. Copy that full value and show it to the owner before creating a client. A developer-mode connection and the public submission draft may have different callback IDs; record each actual value separately.

A stable callback would additionally require correct `iss` on successful and failed responses and exact discovery issuer matching. Do not advertise support solely to obtain a preferred URL. CIMD URLs are also flow-dependent; capture and validate the actual client metadata rather than guessing it.

## Observed portal blocker

After the owner-approved production deployment and successful domain verification, the connection drawer still reports **Authorization unavailable**. Its OAuth selector is disabled; Connect exposes neither an authorization flow nor callback/client fields. A requested rescan failed before tool discovery. OpenAI documents predefined clients, but this portal route has not exposed their configuration. The cause is not proven.

On September 30, the existing personal ChatGPT developer-mode plugin successfully opened the deployed Abbelo permission screen through its previously registered WorkOS client. Neither permission button was clicked. This is evidence that the existing redirect and consent entry point respond, not evidence of token issuance, tools, session execution, or the separate public draft's authentication.

WorkOS Connect configuration currently has both CIMD and DCR disabled. [OpenAI](https://developers.openai.com/plugins/build/auth) and [WorkOS](https://workos.com/docs/authkit/mcp) document CIMD as a supported registration path. A concrete proposal to enable CIMD only is awaiting owner approval. DCR remains off. Enabling CIMD is a hypothesis to test against the public draft, not an established fix. It must retain S256, account-bound explicit consent, resource audience checks, client scope validation, refresh binding and revocation. The existing adapter accepts encoded HTTPS client identifiers in synthetic tests; actual WorkOS-issued CIMD credentials are still untested.

## Proposed registration, not performed

Use a dedicated OpenAI OAuth application, isolated from Cursor/Grok clients, with authorization code, PKCE S256, resource-bound tokens and refresh support. Start with the existing public-client approach (`token_endpoint_auth_method: none`) only if the actual dashboard supports that predefined-client configuration. If the portal requires a secret or a different client profile, stop and present that concrete change for approval; do not create a credential or weaken Abbelo's PKCE requirement.

Copy the exact portal callback. Configure only verified necessary scopes. A WorkOS client scope ceiling is not user permission: the signed token must intersect the explicitly approved local grant. Verify the provider-issued token profile contains the exact expected subject, client, consent-session claim and Abbelo grant claim. Never log token bodies. Keep public client IDs and per-environment endpoint configuration out of the generic distributable. Keep any secret in approved server/portal secret storage only.

## Connection and revocation checks

1. Sign in with the synthetic reviewer account. Cancel the first permission screen and prove no grant/request was prepared.
2. Choose read access and complete WorkOS approval for the correct app. Check four reads; deny both writes even if the token has a broader provider scope.
3. Reconnect with explicit session permission and verify only that new consent expands access. Fresh consent must never modify a different account/client grant.
4. Refresh with the real provider refresh token through the host. Preserve connection identity and exact-retry behavior.
5. Disconnect in Abbelo Settings. Reject both old and refreshed access without reading content or admitting another Run. Determine separately whether host-side removal revokes provider consent; do not equate uninstalling with revocation.

No exact callback or dedicated client has been verified for the public submission draft. The existing personal plugin's registered callback was inspected separately and must not be substituted for that draft. Real token issuance, refresh and revocation remain untested in this preparation.
