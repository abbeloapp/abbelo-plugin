# Verified requirements and evidence

Checked September 30, 2026. Recheck the official pages before submission.

## Official sources

| Source | Application to this candidate |
| --- | --- |
| [Package format](https://developers.openai.com/plugins/build/plugins) | Portable root `plugin.json`, fixed `skills/` and `mcp.json`, OpenAI metadata under `extensions.com.openai`; Codex compatibility supported. |
| [Authentication](https://developers.openai.com/plugins/build/auth) | OAuth authorization code with PKCE; resource discovery, exact issuer and audience; predefined clients supported alongside CIMD/DCR; copy the dashboard callback. |
| [Tool reference](https://developers.openai.com/plugins/reference) | Per-tool OAuth metadata, documented `_meta.securitySchemes` compatibility and `_meta["mcp/www_authenticate"]` error signal. |
| [Submission](https://developers.openai.com/plugins/deploy/submission) | ZIP draft, identity/domain verification, MCP scan, reviewer account, five positive and three negative cases, actual recording, then distinct review and publication. |
| [Submission errors](https://developers.openai.com/plugins/deploy/submission-errors) | Required public HTTPS listing URLs and fields, image constraints and readiness findings. |
| [Guidelines](https://developers.openai.com/plugins/plugin-guidelines) | Truthful listing, minimum data, explicit consequential actions, existing paid-account access only; no digital sales or upgrades through plugin. |
| [Connect and test](https://developers.openai.com/plugins/deploy/connect-chatgpt) | Test MCP in developer mode, then the installed package and skill. Host availability may depend on the account/workspace. |
| [Dots](https://learn.chatgpt.com/docs/dots) | A dot is a separate real host journey; package validity is not evidence that a dot can connect and execute correctly. |
| [Agent Plugins schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json) | Pinned portable manifest schema in `openai/schemas`. |
| [MCP config schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json) | Pinned remote transport schema in `openai/schemas`. |

The local Plugin Creator validator predates portable manifests and some new review fields. This package includes a derived compatibility manifest for that validator and uses the official portable schemas plus task-specific checks for the authoritative submission. Passing either local validator does not mean OpenAI has approved it.

## Observed source behavior

Plugin base: `dfc1efe5dda857e6e62cba0eb4dc3bcce8f26d9e` in `abbeloapp/abbelo-plugin`.
App inspection base: `4f3e6b1800396ad279ee8f5454ab5bb2726dd617` in `abbeloapp/abbelo`.

Six existing tools cover account permissions, entitled work discovery, empty conversation creation, one paid session submission, passive Run polling and saved history. The canonical server verifies resource-bound signed tokens plus current owner, grant, client, consent and Guide access. Retry identity remains stable across refresh of the same connection. A new connection has a different idempotency namespace.

The inspected app handoff originally defaulted to read access and could not newly authorize session execution through that UI. Owner-approved PR #992 is now deployed at merge commit `94c0796ab3883c206d6afe6980fa04e54ae6152f`: it adds explicit read/session choices, retains provider approval, adds per-tool OAuth compatibility and reauthorization metadata, and hosts the exact OpenAI domain challenge. No OAuth credential, client registration, database permission, account scope grant, production flag or issuer setting was changed.

The root plugin README calls Grok end-to-end compatibility unverified. Its files are preserved; no new claim of working Grok or Cursor execution is made. Protocol regression fixtures cover the existing SDK legacy and modern versions, not real clients.

## Public checks

On September 30 the protected-resource metadata and both WorkOS discovery documents returned HTTP 200. The production resource is `https://abbelo.com/mcp`; its issuer is `https://satisfying-gust-31.authkit.app`. PKCE S256 and refresh are advertised. Neither discovery document advertises RFC 9207 issuer response support, DCR nor CIMD support. A missing advertisement is not permission to enable those features.

The website’s `/support`, `/privacy`, `/terms` and `/developers/mcp` URLs responded HTTP 200. This proves reachability, not legal sufficiency, publisher verification, or owner approval. Existing support email is `support@abbelo.com`.

## Data and commerce review

OAuth binds the member’s verified Abbelo identity. WorkOS receives the account ID and verified email for identity linkage. The host receives authorized work summaries, saved messages and completed replies. Approved session text goes to Abbelo’s existing processing pipeline and can save private work. No bulk Guide export, third-party analytics or additional tracking is added by the package.

The owner must verify the privacy policy accurately covers this flow, processors, purposes, retention/deletion and disconnect behavior. The package may use features of an existing paid account. It must not offer checkout, advertise plans, sell Guides or credits, promote upgrades or apply an extra ChatGPT-specific fee. Confirm the `review.commerce` declaration with the owner before setting it. The present toolset has no purchase tools.
