# OpenAI support draft — not sent

Recipient: OpenAI Support, through the official support channel.
Account: hello@abbelo.com.
Subject: Abbelo plugin 0.1.2 uses old CIMD registration despite saved provided-client configuration

Hello,

Abbelo's public plugin draft is blocked on OAuth authorization. Version 0.1.2 uploaded successfully, its metadata and skill checks pass, and the domain is verified. However, the actual Connect request does not use the authentication settings displayed in the portal.

Plugin: plugin_asdk_app_6abda5a4005081918646fb59fb8cc71c
Draft: appsub_6abda5a400808191833c695930b5c6ab
Runtime version: asdk_app_v_41691e2e6364819186d6356da7cee0cd
MCP URL/resource: https://abbelo.com/mcp

Saved 0.1.2 settings:
- client.mode: provided
- clientId: client_01M3JKJDVEWD5X2B368JK6XZ3Q
- tokenEndpointAuthMethod: none
- defaultScopes: ["abbelo:read"]

At 2026-10-12 15:06:08 UTC, the visible Network response from Connect returned an auth_url using:
- client_id: https://chatgpt.com/oauth/1y9f3YO8BNrS/client.json
- scope: openid email offline_access abbelo:read abbelo:write
- redirect_uri: https://chatgpt.com/connector/oauth/1y9f3YO8BNrS
- resource: https://abbelo.com/mcp

We canceled that diagnostic sign-in before authorizing. An earlier attempt at 14:36:36 UTC returned invalid_scope. We have not identified the individual rejected scope. The manual WorkOS client has the matching callback and custom Abbelo scopes, but the observed request is still using the old CIMD client.

Your submission guide says existing client registration can lock credential changes after upload. What is the supported way to rebind this existing draft to its saved provided client and read-only initial scope without deleting the plugin, losing domain verification or broadening WorkOS environment permissions? Please confirm whether the registration is locked or the updated settings are not being applied, and propose the exact fix before changing registrations or grants.

OAuth state, nonce, PKCE challenge values, cookies, credentials and tokens are intentionally omitted. The plugin remains unsubmitted and unpublished.

Thank you,
Matthew
