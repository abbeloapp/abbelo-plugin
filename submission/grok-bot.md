# Grok Bot submission draft

Prepared October 15, 2026. **Not submitted. In-app verification is incomplete.**

Use the [official Grok Bot submission form](https://x.ai/bot/marketplace/submit-a-plugin).
It accepts a public GitHub repository or an MCP endpoint; it does not request a
ZIP. Select **Grok Bot** only for this request. Submission is a review request,
not approval or publication.

## Form values

| Field | Prepared value |
| --- | --- |
| Organization | Abbelo |
| Organization handle | `abbelo` — proposed; availability is unverified |
| Website | https://abbelo.com |
| Logotype | https://raw.githubusercontent.com/abbeloapp/abbelo-plugin/dfc1efe5dda857e6e62cba0eb4dc3bcce8f26d9e/assets/abbelo.png |
| Listing target | Grok Bot |
| Public GitHub repository | https://github.com/abbeloapp/abbelo-plugin |
| MCP endpoint | https://abbelo.com/mcp |
| First name / last name / work email | Publisher to confirm in the form. Do not copy personal account data into this public repository. |
| Test declaration | Leave unchecked until the package has actually worked in the target app. |

Description prepared for the verified release:

> Bring your Abbelo Guides and sessions into Grok Bot. Develop your character, work toward your goals, and pick up where you left off.

Testing-instructions field, after the checks below pass:

> Connect an Abbelo test account using the verified Grok Bot OAuth setup. Find an accessible Guide, approve a session after the credit disclosure, wait for its completed reply, and retrieve the saved conversation. Reads must not spend credits. Retry the same session request with its original ID and arguments and confirm it returns the same Run without a second charge. Verify read-only, revoked, and cross-account access are rejected. Coordinate isolated reviewer access through support@abbelo.com; credentials are provided privately.

This text describes the intended review procedure, not completed tests. Replace
the setup reference with the verified Grok Bot installation instructions before
submission. Never include a token, password, client secret, or real member
conversation in this document or the form's public text.

## Existing package

Candidate inspected: `dfc1efe5dda857e6e62cba0eb4dc3bcce8f26d9e`, version 0.1.0.

- `.cursor-plugin/plugin.json`: existing manifest and required public client-ID variable.
- `mcp.json`: existing remote MCP connection with explicit read/write scopes.
- `skills/abbelo/SKILL.md`: existing permission, session, polling, and retry workflow.
- `assets/abbelo.png`: existing 1024 × 1024 RGB PNG on a white background.
- `LICENSE`: MIT license for the plugin package.

The structure and variable declaration follow the
[Cursor plugin reference](https://cursor.com/docs/reference/plugins).
That is package validation, not evidence that Grok Bot resolves its variables or
completes OAuth. The [README](../README.md) already identifies those preview limits.

## Checks actually performed

Remote sandbox verification at 2026-10-15T15:11:29Z:

| Check | Result |
| --- | --- |
| Manifest and MCP JSON parse; declared client-ID variable matches its reference | Passed |
| Skill frontmatter, license, and referenced logo file exist | Passed |
| Logo is square, opaque PNG with white corner pixels | Passed |
| Protected-resource and OAuth discovery | HTTP 200 |
| Unauthenticated MCP initialization | HTTP 401 with resource-metadata bearer challenge |
| Developer documentation, support, privacy, terms | HTTP 200 |
| Public support page renders its help form | Passed |
| Grok Bot install, sign-in, tool discovery and session completion | Not tested |
| Live refresh, revocation, account isolation, entitlements and charging | Not tested |

[Public endpoint receipt](preflight-2026-10-15.json).

All eight existing MCP backend check scripts passed against application commit
`2ab9b95f089ce06cbb0b5a25e05e74a61aa96ec0` in a remote sandbox. They cover protocol,
authority, consent UI and routes, provider adaptation and lifecycle, privacy,
and service admission. See the [backend check receipt](backend-checks-2026-10-15.json)
for exact commands, output and limitations. These fixture-based checks do not
replace the pending Grok Bot acceptance tests.
No member data was read or AI session run. These checks do not establish
marketplace readiness.

Live issuer metadata advertises PKCE S256, refresh tokens, and client-ID metadata
document support. Abbelo's current public documentation still describes
operator-registered preview clients. Provider metadata alone does not establish
that Grok Bot can obtain a usable Abbelo grant. Verify the actual host flow;
do not infer or invent its callback URL or client ID.

## Required Grok Bot test

Use an isolated reviewer account and synthetic content. The publisher must approve
any new OAuth client or production authentication change before it is made.
Capture the exact callback from Grok Bot's own setup. Cursor's documented
callbacks must not be assumed to be Grok Bot callbacks.

Keep reviewer credentials in a secure private channel. Record the tested package
commit, Grok Bot version, actual setup path, consent scopes, and observed results.

| Case | Expected result | Status |
| --- | --- | --- |
| Connect | Sign-in and consent complete; six Abbelo tools are discovered | Pending |
| Find a Guide | `abbelo_find_work` with kind `program` returns only entitled Guides; no credit use | Pending |
| Start a session | With separate paid-work consent, create a conversation using a returned `programId`, submit the exact member message, and poll to completion | Pending |
| Continue and retrieve | A second authorized turn retains context; saved conversation and replies can be retrieved without additional read charges | Pending |
| Refresh and replay | Refresh preserves access; identical request ID and arguments return the original Run with no duplicate charge | Pending |
| Read-only consent | Session submission is denied without write permission | Pending |
| Disconnect / expiry | Revoked or expired authority cannot read or run work; refresh does not restore a revoked grant | Pending |
| Foreign account / inaccessible Guide | Another account's work and an unentitled Guide are rejected without disclosure or charging | Pending |

The MCP tools do not supply a per-call credit cap. Agree on the test account,
messages, and a verified spend limit before paid tests; do not promise a cap the
system cannot enforce.

## Publisher decisions and final submission

1. Complete the Grok Bot test and record evidence. Resolve setup failures first.
2. Confirm the publisher contact and available organization handle.
3. Review the [Publisher Terms](https://cursor.com/marketplace-publisher-terms).
   Section 3.1 addresses direct and indirect plugin fees; Abbelo sessions consume
   credits. Obtain clarification on the existing paid-service model instead of
   assuming an exception. Section 6.3 also restricts model training on plugin data.
4. The owner completes legal declarations and sensitive sign-in. The form's test
   declaration must reflect actual testing.
5. Submit through the official form, then retain its confirmation or reference.
   Record approval or public availability only after separate verification.

Public product links: [Support](https://abbelo.com/support),
[Privacy](https://abbelo.com/privacy), [Terms](https://abbelo.com/terms).
