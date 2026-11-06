# Abbelo

Use your existing Abbelo Goals and Library Guides from an AI app. The host conducts the conversation; Abbelo supplies authorized data and saves requested notes.

## Integration preview

This package targets MCP contract 2.1.0 at [Abbelo’s MCP endpoint](https://abbelo.com/mcp). A running endpoint or installed package does not establish a working host connection or marketplace approval. Verify OAuth consent, tool discovery, refresh and disconnect in the intended host using an isolated test account. Dots, Muse, Grok Bot and OpenAI compatibility must each be proven before advertising support.

## Setup

Use the host’s supported OAuth flow and [Abbelo’s protected-resource metadata](https://abbelo.com/.well-known/oauth-protected-resource/mcp). For this Cursor-format package, configure `ABBELO_CLIENT_ID` with the public PKCE client registered for the host and its exact callbacks. Verify variable resolution in that host; this is not a universal setup format. Do not substitute another app’s client or ask a member to paste keys or tokens into chat.

Check `abbelo_get_connection` after connecting. Optional **Save to Goals** consent permits the note tool; older grants must reconnect to receive that permission.

## Tools

| Tool | Purpose |
| --- | --- |
| `abbelo_get_connection` | Check effective permissions and note-write capability. |
| `abbelo_find_work` | Find Goals, accessible Library Guides, or saved conversations. |
| `abbelo_get_goal` | Read the current plan, course overview, next step and session focus. |
| `abbelo_read_guide` | Browse contents and read exact authorized passages. |
| `abbelo_search_guide` | Find passages within a Guide’s entitled edition. |
| `abbelo_get_goal_notes` | Read attributed notes from connected apps. |
| `abbelo_save_goal_note` | Save a requested report or summary to existing Goals work. |
| `abbelo_get_conversation` | Read the exact saved conversation requested. |
| `abbelo_open_session` | Get the native player link for an authorized saved conversation. |
| `abbelo_get_run` | Read a historical recorded result without executing AI. |

Use `goal`, `guide` or `conversation` for discovery. `growth` and `program` are compatibility aliases. The first-party product is currently called Goals.

Examples: “Open my leadership goal and help me with the current step.” “Find what this Guide says about delegation.” “Save what I just told you as a note on this goal.”

## Permissions and limitations

`abbelo:read` grants account-wide personal access, subject to current ownership and Guide entitlement. Optional `abbelo:write` with fresh `goals-guides-v2` consent allows attributed notes. It does not authorize a teammate’s private data. Notes distinguish a client-reported member statement from an agent summary and never claim verified speech, completed practice or achievement.

For live voice, `abbelo_open_session` returns a link to the exact saved conversation in Abbelo. The member signs in and starts voice there; opening the link does not start audio or spend credits. The voice player does not run inside the host.

The tools do not create Goals, prepare or advance courses, publish Guides, buy content, generate voice or change billing. The retired `abbelo_start_conversation` and `abbelo_continue_session` tools must not be used. Open Abbelo for unsupported actions.

Current tools call no Abbelo generation provider and spend no Abbelo AI credits. Host model usage follows that host’s subscription and terms; Abbelo voice and Metis preparation are separate. Never imply one subscription pays for every service.

Use the same UUID and identical arguments to retry a note save. After reconnecting, read notes and reconcile an uncertain save before starting another. Disconnect in Abbelo Settings to revoke access; uninstalling a plugin alone does not revoke a grant. External apps may retain already delivered data under their own policies.

The package has no local executable, analytics, shell hooks or credential store. Follow the [current contract](https://abbelo.com/developers/mcp) and [host skill](skills/abbelo/SKILL.md).

[Privacy](https://abbelo.com/privacy) · [Terms](https://abbelo.com/terms) · [Usage policies](https://abbelo.com/usage-policies)

## License

The plugin configuration, documentation and skill are MIT licensed. Abbelo branding remains Abbelo’s; this license does not grant trademark rights or license Guide content, member data or the hosted service.
