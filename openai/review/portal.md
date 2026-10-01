# Official portal walkthrough and approval boundaries

Source: [OpenAI's submission guide](https://developers.openai.com/plugins/deploy/submission), checked September 30, 2026. The owner completed Business verification. Version 0.1.0 was uploaded as a private draft under **Business — Abbelo**. Metadata reports **No Issues** and the workflow skill reports **Checks passed**. No review submission or publication was performed.

The current blocker is domain verification. The exact challenge file is prepared in app PR #992 and needs production deployment approval. The callback and OAuth client remain unconfigured. The review form defaults to All supported countries; this has not been confirmed or saved as an owner declaration.

## Preparation and draft setup

1. Open [organization settings](https://platform.openai.com/settings/organization/general). The owner chooses the legal individual/business identity and completes required verification. Do not invent a country, company name, address, payment detail or legal declaration. Required verification documents remain with the owner.
2. In [Plugins](https://platform.openai.com/plugins), select **Upload new or existing plugin**. Choose the verified developer identity and the reviewed ZIP. Upload creates a draft; it is not approval or publication. Use the owner-authorized draft package; approval to submit for review and publish remains separate.
3. In **Metadata & Skills**, inspect the listing, cases and automated findings. Confirm publisher identity, category, country availability and the four public URLs. Resolve package findings in source and reupload.
4. In **MCPs**, choose Abbelo and **Connect**. Record the exact displayed callback/client requirements. Obtain approval for the specific WorkOS client registration before creating credentials or changing production authentication.
5. Record the domain challenge and exact portal URL. Prepare the file change, then obtain production deployment approval before hosting the token. Never overwrite another plugin's verification token. Deployment and successful challenge readback are separate evidence.
6. Authenticate the synthetic review account and inspect all six scanned tools, scopes and annotations. Correct issues and rescan. No paid tool call until its bounded test plan is approved.
7. Follow `acceptance.md` and `demo.md`. Enter test credentials only through secure **Review details**. Add the real reviewed recording URL to the package, rebuild and reupload. Preserve the fixture for future reviews.

## Submit for review

After every readiness gate passes, show the owner the final package hash, exact listing, country/commerce declarations, complete case results, demo and portal findings. Ask approval before **Submit for review**. The owner must review and approve any legal/policy attestations. A submitted draft is only under review, not approved or live.

## Publish after approval

Wait for OpenAI's decision. Resolve any feedback without claiming acceptance. Once approved, obtain a separate owner decision to **Publish plugin**. Verify the public listing and real member installation after publication. Do not turn a local validation success, uploaded draft or review email into a claim of publication.
