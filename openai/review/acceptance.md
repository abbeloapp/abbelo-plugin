# Acceptance plan and evidence ledger

**Actual ChatGPT and dot test status: NOT RUN. No paid test was authorized or performed.** Local fixtures are synthetic. Historical sandbox/Claude receipts do not prove this integration.

## Reviewer fixtures needed

Use a dedicated synthetic member account A and a separate account B. Never use the owner's real Goals, chats or documents for a public demo. Account A needs an entitled, safely licensed communication Guide and enough approved credits for the test. Account B needs one private conversation. Keep one known Guide inaccessible to A. Record these IDs in private test notes, not the package or public recording. Public prompts resolve names with `abbelo_find_work`; do not guess IDs.

The reviewer account must work without a personal MFA approval, email/SMS code, magic link, VPN or private network. Do not disable real-user security controls to create reviewer access. The owner must approve a suitable account strategy if current signup cannot provide that. Put credentials only in the portal's secure Review details.

## Requested paid scope, awaiting approval

Two session messages per host run the paid positive cases, first session and continuation. Four messages cover ChatGPT and a dot, if each host is tested separately. Repeat transport calls only with identical request IDs and arguments. Eight public review scenarios must then be demonstrated against the reviewer fixture. Read and denial cases must never admit paid work.

Before execution, show the owner the selected account, exact two messages from the manifest, proposed maximum number of new Runs, and an enforceable total credit limit. The six MCP tools do not expose cost estimates or an enforceable per-call cap. Establish the bound using existing account/server controls and passive ledger measurements; if that cannot be done, stop and obtain approval for a clearly described alternative. Never claim a local request counter enforces a currency or credit limit.

## Required real host matrix

| Check | Evidence to retain privately | Current status |
| --- | --- | --- |
| Install portable ZIP with skill and MCP | Package hash/version, host version, tools discovered, skill selection | Not run |
| Sign in, cancel, read consent, session consent | Correct app/account, approved scopes, no automatic write grant | Not run |
| Guide discovery and selection | Returned IDs, entitled source context; inaccessible Guide denial | Not run |
| Start empty conversation | Conversation ID and zero AI ledger delta | Not run |
| First session execution | Approved message, request ID, one Run, final reply and actual credit delta | Not run |
| Poll queued/running Run | Same Run, no new execution from reads | Not run |
| Continue session | Same conversation ID, new request ID, preserved authorized context | Not run |
| Open Abbelo Home | Exact returned conversation ID, both turns visible together | Not run |
| Saved-result read | Saved text matches and zero new Run/credit delta | Not run |
| Lost acknowledgement / exact replay | Same connection, ID and arguments return same Run; one charge only | Not run |
| Changed-input replay | Same request ID + changed message is refused, no second charge | Not run |
| Real token refresh | Fresh provider token, same owner/client/connection and stable replay identity | Not run |
| Reconnect to new connection | Do not replay a paid request blindly; reconcile saved Run/history first | Not run |
| Cross-account direct IDs | No content leak, Guide access failure before admission | Not run |
| Disconnect/revocation | Old and refreshed credentials denied; no new work | Not run |
| Dot background approval | No paid loop or implicit spend based on installation/connection | Not run |
| Cursor and Grok regression | Existing client auth/read/write/retry behavior retained | Not run |

Record the five positive and three negative cases in `plugin.json` individually as pass/fail, with tool traces and observed outcomes. Tool traces must redact access/refresh tokens, cookies, passwords, OAuth codes, member emails and private content. Keep raw secrets out of Git and the ZIP. Do not mark a case passed from a script that only asserts prompt text.

## Safe fixture coverage already available

The companion app's `npm run check:mcp` exercises signed identity/resource/client/consent binding, local scope intersection, revocation, owner and Guide boundaries, exact replay semantics, passive polling, safe errors, explicit permission choices, React account-switch races, duplicate prevention and SDK legacy/modern discovery. Database fixtures and the full build add SQL and Home presentation coverage. These prove mechanics with synthetic provider responses; a live host run remains mandatory.

## Stop conditions

Stop on unexpected account identity, unrequested scope expansion, inaccessible Guide material, a charge from a read, two Runs/charges for one exact request, missing saved results, inaccessible reviewer sign-in, unknown usage or a cost beyond the approved bound. Do not automatically create a replacement paid Run to recover a failure. Preserve evidence and report the specific failing boundary.
