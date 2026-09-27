# Abbelo

Bring your personal work in Abbelo into your conversations. Find accessible Guides, continue saved conversations, and work on skills and habits with Abbelo.

## Preview status

This is a plugin package for integration review. Abbelo's production MCP endpoint is in controlled verification. General client registration is not open, and end-to-end compatibility with Grok Bot has not yet been verified. This repository is not an approved marketplace listing or a claim of public availability.

The endpoint and OAuth discovery are live. Connecting requires a public PKCE client registered by Abbelo, a verified Abbelo account, and the member's explicit consent. Contact support@abbelo.com for preview coordination. Do not substitute an unrelated OAuth client, API key, or another person's token.

## Setup for a registered preview

1. Coordinate the host's exact OAuth callback URLs and client registration with Abbelo. Cursor documents separate web/agent and desktop callbacks; verify the actual Grok Bot callback before registering it.
2. Configure the required `ABBELO_CLIENT_ID` plugin variable with the registered public client ID. The package uses Cursor's plugin-variable mechanism in `mcp.json`; its resolution and OAuth flow must be tested in Grok Bot before release.
3. Install the plugin for testing using the host's supported plugin flow, then authenticate through Abbelo's consent screen. No client secret or member access token belongs in this repository or in chat.
4. Verify `abbelo_get_connection` before reading or submitting personal work.

The connection uses Streamable HTTP at `https://abbelo.com/mcp`. Discover OAuth metadata from `https://abbelo.com/.well-known/oauth-protected-resource/mcp`.

## What it provides

| Tool | Purpose |
| --- | --- |
| `abbelo_get_connection` | Check the current connection and permissions. |
| `abbelo_find_work` | Find accessible conversations, Goals, or Guides. |
| `abbelo_start_conversation` | Create a saved conversation, optionally with a Goal or Guide. |
| `abbelo_continue_session` | Send a message for Abbelo to work on. This can use Abbelo credits and update saved personal work. |
| `abbelo_get_run` | Read the status and completed reply for a submitted message. |
| `abbelo_get_conversation` | Read permitted saved conversation history. |

Guide identifiers use the API's compatibility field `programId` and search kind `program`. They are shown to users as Guides.

Example requests after successful connection:

- Find a Guide I can use to practice clear communication.
- Continue my Abbelo conversation about building a reading habit.
- Start an Abbelo session to help me prepare for a difficult conversation.

## Permissions, data, and credits

`abbelo:read` permits reading the connection, accessible work summaries, saved conversation history, and results. `abbelo:write` permits creating conversations and submitting sessions that can consume Abbelo credits and save changes. A selected Goal or Guide does not narrow the account-wide personal-work permission.

The plugin exposes no purchases, account administration, raw Guide files, or bulk exports. It contains no local executable, analytics, shell hooks, or credential store. The host and Abbelo process authorized requests under their respective policies.

Only `abbelo_continue_session` submits AI work. Finding work, creating a conversation, polling, and reading history do not use AI credits. A failed session may still have incurred provider costs. Keep the same request ID and exact arguments when retrying an uncertain write.

Removing a plugin or closing a transport session is not the same as revoking its Abbelo grant. Contact support@abbelo.com for connection and account help during the preview.

## Verification required before release

- Register the intended host's exact redirect URLs and configure its public client ID.
- Verify plugin-variable resolution, consent, OAuth scopes, and authenticated tool discovery in Grok Bot.
- Verify a permitted read and a separately authorized write, saved reply, retry behavior, and credit accounting using an isolated test account.
- Verify revocation and rejection of unauthorized access.
- Complete marketplace review. Do not advertise approval before it is granted.

## Links

- [Abbelo](https://abbelo.com)
- [MCP contract](https://abbelo.com/developers/mcp)
- [Privacy](https://abbelo.com/privacy)
- [Terms](https://abbelo.com/terms)
- [Usage policies](https://abbelo.com/usage-policies)
- [Cursor plugin submission requirements](https://cursor.com/docs/reference/plugins#submitting-a-plugin)
- [Cursor static OAuth configuration](https://cursor.com/docs/mcp#static-oauth-for-remote-servers)

## License

The plugin configuration, documentation, and skill are MIT licensed. Abbelo's name and logo remain Abbelo branding; the license does not grant trademark rights or permission to imply endorsement. The plugin license does not license Guide content, member data, or Abbelo's hosted service.
