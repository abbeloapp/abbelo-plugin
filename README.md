# Abbelo

Explore Library Guides, create and manage Studio Guides, and continue existing Goals work from a connected AI app. The host conducts the conversation; Abbelo supplies authorized data and its existing Studio processing.

## Integration preview

This package targets MCP contract 3.0.0 at [Abbelo’s MCP endpoint](https://abbelo.com/mcp). A running endpoint or installed package does not establish a working host connection or marketplace approval. Verify OAuth consent, tool discovery, refresh and disconnect in the intended host using an isolated test account. Dots, Muse, Grok Bot and OpenAI compatibility must each be proven before advertising support.

## Setup

Use the host’s supported OAuth flow and [Abbelo’s protected-resource metadata](https://abbelo.com/.well-known/oauth-protected-resource/mcp). For this Cursor-format package, configure `ABBELO_CLIENT_ID` with the public PKCE client registered for the host and its exact callbacks. Verify variable resolution in that host; this is not a universal setup format. Do not substitute another app’s client or ask a member to paste keys or tokens into chat.

Check `abbelo_get_connection` after connecting. New connections disclose Studio draft access. The optional **Create and update** switch enables Guide creation, imports, editing, publication and Goal notes. Older grants retain their original permissions and must reconnect for Studio access.

## Tools

| Tool | Purpose |
| --- | --- |
| `abbelo_get_connection` | Check effective Studio and note permissions. |
| `abbelo_find_work` | Find Goals, accessible Library Guides, or saved conversations. |
| `abbelo_get_goal` | Read the current plan, course overview, next step and session focus. |
| `abbelo_read_guide` | Browse contents and read exact authorized passages. |
| `abbelo_search_guide` | Find passages within a Guide’s entitled edition. |
| `abbelo_get_goal_notes` | Read attributed notes from connected apps. |
| `abbelo_save_goal_note` | Save a requested report or summary to existing Goals work. |
| `abbelo_get_conversation` | Read the exact saved conversation requested. |
| `abbelo_get_run` | Read a historical recorded result without executing AI. |
| `abbelo_open_session` | Return a link to the exact saved conversation in Abbelo’s native voice player. |
| `abbelo_list_studio_guides` / `abbelo_get_studio_guide` | Find owned drafts and inspect current metadata, sources and revision. |
| `abbelo_create_guide` / `abbelo_update_guide` | Create a private draft and save requested edits. |
| `abbelo_prepare_guide_upload` / `abbelo_complete_guide_upload` | Transfer and attach original files, then prepare readable material. |
| `abbelo_import_guide_link` / `abbelo_get_guide_import` / `abbelo_finish_guide_import` | Start, inspect and complete a saved YouTube import. |
| `abbelo_set_guide_publication` | Publish or unpublish with the person’s explicit visibility choice. |

Use `goal`, `guide` or `conversation` for discovery. `growth` and `program` are compatibility aliases. The first-party product is currently called Goals.

Examples: “Open my leadership goal and help me with the current step.” “Find what this Guide says about delegation.” “Save what I just told you as a note on this goal.”

## Studio workflow

Check `canUseStudio` and `canWriteStudio`. Create a private draft, then add authored text or upload original files. Transfer file bytes with raw HTTP PUT to each returned signed URL and complete the upload using the exact descriptors. Keep signed URLs private. If the host cannot transfer files, offer the Studio editor link rather than claiming the upload succeeded.

For YouTube imports, retain the import ID, poll its saved status and finish when complete. Pending is not ready. Reuse request IDs on retries, inspect uncertain saves, and never duplicate a paid provider operation. Read the latest revision before edits or publication. Publish only at the person’s explicit request with their chosen public, unlisted or private visibility.

## Permissions and limitations

`abbelo:read` grants account-wide personal access, subject to current ownership and Guide entitlement. Current `studio-guides-v3` consent includes Studio reads; optional `abbelo:write` permits Guide changes and attributed notes. Version 2 grants can still save notes but cannot use Studio. It does not authorize a teammate’s private data. Notes distinguish a client-reported member statement from an agent summary and never claim verified speech, completed practice or achievement.

For live voice, `abbelo_open_session` returns a link to the exact saved conversation in Abbelo. The member signs in and starts voice there; opening the link does not start audio or spend credits. The voice player does not run inside the host.

The tools do not create Goals, prepare or advance courses, buy content, generate voice inside the host or change billing. The retired `abbelo_start_conversation` and `abbelo_continue_session` tools must not be used. Open Abbelo for unsupported actions.

Library reads and notes spend no Abbelo AI credits. Studio preparation uses Abbelo’s existing providers and admission rules; this release adds no member credit charge. Host model usage follows that host’s terms. Abbelo voice and Metis preparation are separate; never imply one subscription pays for every service. Disclose any future Abbelo charge before starting the work.

Use the same UUID and identical arguments to retry a note save. After reconnecting, read notes and reconcile an uncertain save before starting another. Disconnect in Abbelo Settings to revoke access; uninstalling a plugin alone does not revoke a grant. External apps may retain already delivered data under their own policies.

The package has no local executable, analytics, shell hooks or credential store. Follow the [current contract](https://abbelo.com/developers/mcp) and [host skill](skills/abbelo/SKILL.md).

[Privacy](https://abbelo.com/privacy) · [Terms](https://abbelo.com/terms) · [Usage policies](https://abbelo.com/usage-policies)

## License

The plugin configuration, documentation and skill are MIT licensed. Abbelo branding remains Abbelo’s; this license does not grant trademark rights or license Guide content, member data or the hosted service.
