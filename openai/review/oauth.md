# OAuth setup: pending exact dashboard values and approval

Do not use a sample callback or a Cursor client ID. Do not enable DCR/CIMD to bypass registration. Do not share an owner's token or put secrets in the ZIP.

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

A stable callback would additionally require correct `iss` on successful and failed responses and exact discovery issuer matching. Do not advertise support solely to obtain a preferred URL. CIMD URLs are also flow-dependent; this candidate intentionally stays with operator registration.

## Observed portal blocker

After the owner-approved production deployment and successful domain verification, the connection drawer still reports **Authorization unavailable**. Its OAuth selector is disabled; Connect exposes neither an authorization flow nor callback/client fields. A requested rescan failed before tool discovery. OpenAI documents predefined clients, but this portal route has not exposed their configuration. The cause is not proven. Do not substitute a guessed callback, place credentials in the package, or enable DCR/CIMD to work around this. Resolve the supported configuration path before proposing the exact client registration.

## Proposed registration, not performed

Use a dedicated OpenAI OAuth application, isolated from Cursor/Grok clients, with authorization code, PKCE S256, resource-bound tokens and refresh support. Start with the existing public-client approach (`token_endpoint_auth_method: none`) only if the actual dashboard supports that predefined-client configuration. If the portal requires a secret or a different client profile, stop and present that concrete change for approval; do not create a credential or weaken Abbelo's PKCE requirement.

Copy the exact portal callback. Configure only verified necessary scopes. A WorkOS client scope ceiling is not user permission: the signed token must intersect the explicitly approved local grant. Verify the provider-issued token profile contains the exact expected subject, client, consent-session claim and Abbelo grant claim. Never log token bodies. Keep public client IDs and per-environment endpoint configuration out of the generic distributable. Keep any secret in approved server/portal secret storage only.

## Connection and revocation checks

1. Sign in with the synthetic reviewer account. Cancel the first permission screen and prove no grant/request was prepared.
2. Choose read access and complete WorkOS approval for the correct app. Check four reads; deny both writes even if the token has a broader provider scope.
3. Reconnect with explicit session permission and verify only that new consent expands access. Fresh consent must never modify a different account/client grant.
4. Refresh with the real provider refresh token through the host. Preserve connection identity and exact-retry behavior.
5. Disconnect in Abbelo Settings. Reject both old and refreshed access without reading content or admitting another Run. Determine separately whether host-side removal revokes provider consent; do not equate uninstalling with revocation.

No exact callback, dedicated client, real token issuance, refresh, or revocation has been verified for OpenAI in this preparation.
