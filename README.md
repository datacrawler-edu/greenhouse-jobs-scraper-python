# Greenhouse jobs scraper: Python API examples and CSV export

Collect public vacancies from Greenhouse company boards using the hosted [Greenhouse Jobs Scraper](https://apify.com/datascraperes/greenhouse-jobs-scraper?fpr=edudata). This repository provides API integrations and real sample data; the hosted service performs collection.

## What this repository helps you do

- Collect jobs from company board URLs or tokens.
- Combine multiple boards in one run with explicit output limits.
- Read optional descriptions, departments, offices and application links.
- Export an existing Dataset without starting another collection.

## Example result

A projection of an actual collected posting:

```json
{
  "boardSlug": "airbnb",
  "sourceJobId": "7789554",
  "title": "Associate Legal Counsel, Japan",
  "location": "Tokyo, Japan"
}
```

[Complete sample records](data/sample-output.json) contain three jobs collected with the [sample input](data/sample-input.json). The [CSV sample](data/sample-output.csv) selects eight spreadsheet-friendly columns. Vacancies can change after collection.

## Run without code

1. Open [the Actor](https://apify.com/datascraperes/greenhouse-jobs-scraper?fpr=edudata).
2. In **Input**, enter an Greenhouse company board URL, such as `https://job-boards.greenhouse.io/airbnb`, or its token `airbnb`.
3. Set per-board and total job limits, review pricing, and click **Start**.
4. Inspect the **Dataset** and the `SUMMARY` and `ERRORS` records in the run's key-value store.
5. Export the Dataset as JSON or CSV.

See the [no-code guide](docs/no-code-guide.md).

## Try it with Apify's free plan

Apify offers a Free plan with $5 in monthly prepaid usage and no credit card required. Available credit can cover a small test; usage is not unlimited. Unused credits expire at the end of the billing cycle. Check [current platform pricing](https://apify.com/pricing?fpr=edudata).

## Quick start for developers

Use Python 3.11 or newer. The Python examples require no third-party packages.

```bash
export APIFY_API_TOKEN="your-token"
python examples/python/collect_jobs.py
```

Windows PowerShell:

```powershell
$env:APIFY_API_TOKEN = "your-token"
python examples/python/collect_jobs.py
```

The example writes `greenhouse-jobs.json` and prints the run ID and collection summary. Exit code 2 means incomplete or unknown coverage; available rows remain in the file. A transport failure can interrupt downloading: use the printed run ID to recover the Dataset before starting another run.

## Input example

```json
{
  "boardUrls": [
    "airbnb"
  ],
  "includeContent": true,
  "maxJobsPerBoard": 3,
  "maxTotalJobs": 3,
  "continueOnError": true
}
```

See the [input reference](docs/input-reference.md). There is no global company or keyword search.

## Request examples

- [Python single board](examples/python/collect_jobs.py): three jobs, saved as JSON.
- [Python multiple boards](examples/python/batch_boards.py): Airbnb and Stripe, at most five jobs each and ten overall.
- [Python existing-Dataset export](examples/python/export_jobs_csv.py): export up to 1,000 existing rows without starting a new run.
- [JavaScript](examples/javascript/request.mjs): Node.js 20+, no packages to install; run `node examples/javascript/request.mjs`.
- [cURL](examples/curl-request.md): start once, inspect status, then retrieve output.

Collection examples set a five-minute server timeout and a $0.05 maximum Actor charge. Infrastructure or other platform charges can apply separately. HTTP requests time out after 30 seconds; polling has a watchdog. An uncertain start request is not retried automatically because it might already have created a run.

## Output fields

| Field | Meaning |
| --- | --- |
| `boardSlug`, `boardUrl` | Company board identity |
| `sourceJobId` | Posting identity within its board |
| `title`, `location`, `locations` | Role and published locations |
| `department`, `team` | Employer-provided organization information |
| `offices`, `metadata` | Available employer-published office and metadata detail |
| `jobUrl`, `applyUrl` | Public posting and application links |
| `descriptionHtml`, `descriptionText` | Optional descriptions |
| `updatedAt`, `language` | Available posting update and language information |
| `postedAt`, `scrapedAt` | Publication and collection timestamps |

See the [complete field reference](docs/output-reference.md). Null or empty optional values do not imply a missing posting.

## Common use cases

Use the examples for [job directories, hiring monitoring and description analysis](docs/use-cases.md). Compare snapshots with `(boardSlug, sourceJobId)` as the identity; a fresh run creates a fresh snapshot.

## Collect Greenhouse jobs from multiple company boards with Python

Run `python examples/python/batch_boards.py`. Put known board URLs or tokens in `boardUrls`; the total output limit applies in input order. `continueOnError` allows other boards to be processed when one is unavailable. Check the summary before treating a snapshot as complete.

## Export an existing Greenhouse jobs Dataset to CSV

```bash
python examples/python/export_jobs_csv.py YOUR_DATASET_ID --output jobs.csv
```

This reads existing rows only, with an explicit 1,000-row example limit. It does not create a run or new job-result events; storage transfer charges may apply. The CSV contains selected columns and protects spreadsheet cells that could otherwise be interpreted as formulas.

## Read Greenhouse job descriptions as text and HTML

Set `includeContent` to `true`. Use `descriptionText` for downstream analysis and `descriptionHtml` when you need the published formatting. Departments and offices depend on what the board provides; missing optional information is not inferred.

## FAQ

Read the [FAQ](docs/faq.md) for unavailable boards, partial runs, optional fields and result limits.

## Limits and pricing

Supply 1–50 boards. `maxJobsPerBoard` accepts 1–5,000 and `maxTotalJobs` accepts 1–50,000; defaults are 500 and 5,000 respectively. These are ceilings, not promises of that many live postings. The examples intentionally use smaller limits.

Billing is pay per event: one unique job confirmed in the Dataset is one `job-result` event. Rates depend on the Apify tier:

| Tier | Price per job-result event | Equivalent per 1,000 jobs |
| --- | --- | --- |
| Free | $0.001 | $1.00 |
| Bronze | $0.0009 | $0.90 |
| Silver | $0.0008 | $0.80 |
| Gold | $0.00075 | $0.75 |
| Platinum | $0.00075 | $0.75 |
| Diamond | $0.00075 | $0.75 |

Descriptions and office details do not add extra result events. Jobs saved before another board fails remain billable. Check the live [Actor Pricing tab](https://apify.com/datascraperes/greenhouse-jobs-scraper?fpr=edudata) before running; platform charges and account limits can also apply.

A spending cap can stop collection before the requested limits. `SUCCEEDED` alone does not establish completeness: require `SUMMARY.complete` and inspect board errors. Missing summary means coverage is unknown. Even a complete limited run does not mean every job on the board was collected.

## Hosted version

Use [Greenhouse Jobs Scraper on Apify](https://apify.com/datascraperes/greenhouse-jobs-scraper?fpr=edudata) for the hosted collection, Dataset storage and API access. You need an Apify API token for programmatic examples; company board access does not require a Greenhouse account.

## Responsible use

Respect applicable terms, employer rights and privacy obligations. This independent integration is not affiliated with Greenhouse. It does not submit applications or collect applicant information. Keep API tokens out of files and commits. Links to Apify include the `fpr=edudata` referral parameter.

## Support

For integration issues, [open a GitHub issue](https://github.com/datacrawler-edu/greenhouse-jobs-scraper-python/issues). For collection issues, use the Actor's Issues tab and include the run ID, affected board and non-sensitive input. Never share your API token.

## License

Examples and documentation are MIT licensed. See [LICENSE](LICENSE). This license does not grant rights over third-party job content.
