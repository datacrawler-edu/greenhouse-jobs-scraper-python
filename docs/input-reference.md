# Greenhouse input reference

| Field | Default | Accepted values and behavior |
| --- | --- | --- |
| `boardUrls` | Required | 1–50 public Greenhouse board URLs or tokens; duplicate tokens are processed once ignoring case. |
| `includeContent` | `true` | Boolean; include HTML and readable text descriptions, departments and offices where available. |
| `maxJobsPerBoard` | `500` | Integer 1–5,000; maximum unique jobs saved from each board. |
| `maxTotalJobs` | `5000` | Integer 1–50,000; total maximum across boards in input order. |
| `continueOnError` | `true` | Boolean; continue after a board problem. False stops later boards while preserving already saved rows. |

See the [complete input example](../data/sample-input.json). Unknown fields are rejected. Use a public board URL such as `https://job-boards.greenhouse.io/airbnb` or the token `airbnb`. Generic company careers pages and global company or keyword discovery are not supported.

Limits control saved output; they are not a promise that employers publish that many jobs. Platform timeout and charge limits are run options, not Actor input fields.
