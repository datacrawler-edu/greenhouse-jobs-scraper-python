# FAQ

## Can I search all Greenhouse companies by keyword?

No. Supply company board URLs or tokens. Filtering returned records in your workflow does not change which collected jobs are billable.

## Why are some fields null?

Employers do not supply every optional field. Use `boardSlug` for board identity and `sourceJobId` for the posting. See the [output reference](output-reference.md).

## Are salaries always available?

No. Salary text can be included in a description, but the Actor does not guarantee a structured salary range. Retain the full description for downstream analysis.

## Does SUCCEEDED mean every board was collected?

No. Source problems can produce a partial or stopped collection while preserving available rows. Inspect `SUMMARY.complete`, `status`, `failedBoards`, `limitedBoards` and `ERRORS`. Missing summary leaves completeness unknown. Complete within configured limits is not the same as all jobs on every board.

## Why do collection examples exit with code 2?

That code means incomplete or unknown coverage. Available downloaded rows are retained. Inspect the printed run ID before repeating a request. Transport or download errors may stop the script before a local file is written, while the remote Dataset remains available.

## Can a run still fail?

Yes. Storage integrity problems or unresolved delivery/billing can stop execution. Review saved data before retrying. No integration can guarantee that a third-party service or network will always respond.

## What do the example limits protect?

Collection scripts set a five-minute server timeout, a $0.05 maximum Actor charge and small output limits. They use bounded HTTP requests and a polling watchdog. Platform charges may apply separately. A watchdog requests an abort; check Console if that request itself fails.

## Can I collect more jobs?

Yes, within the input limits. Change collection and download limits together to avoid silently truncating a larger Dataset. Collection examples download at most 100 rows, enough for both sample workloads. Existing-Dataset CSV export has its own 1,000-row example limit.

## Do I need an Greenhouse account?

No Greenhouse login is required for public boards. API examples require an Apify account and token. The Actor does not submit applications.
