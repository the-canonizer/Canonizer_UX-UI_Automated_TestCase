# Remaining Test Gaps

This file tracks scenarios from the large missing-test list that are not yet fully covered in `main.py`.

## Added In Recent Passes (Now Covered)

- Login modal close, forgot-password invalid email/blank email/unregistered email
- Forgot-password OTP invalid code/blank code/resend OTP
- Reset password mismatch
- Topic create trailing spaces, enter key, mandatory asterisk, cancel create
- Topic preview open/cancel/submitter link
- Topic comparison (base compare, agreement link, create camp, create topic, back button, view version)
- Topic with only mandatory fields
- Camp statement cancel/preview
- Camp creation/management: mandatory asterisk, cancel create, create with mandatory fields, update with valid data
- Camp update flows: submit update entry, preview fields/cancel/submitter nickname, compare versions, comparison labels
- Forum filter tabs: my threads, participation, top 10
- Forum post actions: edit post, delete post
- News add with enter key, edit-news load/cancel/blank fields/valid/invalid/trailing spaces
- Browse only-my-topics, namespace filter, algorithm filter trigger, topic-tag search trigger
- Notifications matrix (filters, mark-all cancel, delete-all cancel, load-more when available)
- Supported camps management (direct/delegated search and remove-support cancel modal)
- Preferences topic-tag search
- Social auth settings controls visibility
- Upload file manager (search/reset, list-grid toggle, action menu visibility, delete modal cancel)
- Advanced search (sidebar tab navigation, asof route filters, pagination visibility)

## Remaining But Feasible With Existing Methods (Likely Next)

- No currently identified low-risk remaining items using existing stable page-object methods.

## Needs New Page-Object Methods / Locators (Not Safe To Add Yet)

- Advanced support management (reorder persistence, petitions, full remove/confirm data-safe flows)
- Full notifications matrix (single-item read behavior, confirmed mark-all/delete-all with deterministic fixtures)
- AI agents workflows (register/edit/password/deactivate/guide actions)
- Advanced search deeper filter-combination assertions (algorithm/score/date interaction with result counts)
- Rich file manager flows (confirmed delete/download/rename persistence, sort assertions, deterministic fixtures)
- Preferred topics/tag preference save/discard validation and wizard finish/skip flows
- Social account link/unlink from account settings (live provider callback and unlink confirmation)

## Notes

- Some existing helper methods are present but rely on brittle selectors and should be stabilized before scaling those test areas.
- Duplicate test-name overrides in `main.py` were already fixed in recent updates.
