# Greenhouse output reference

One Dataset item represents one posting. Use `(boardSlug, sourceJobId)` as identity. See the [complete real sample](../data/sample-output.json).

| Field | Type | Meaning |
| --- | --- | --- |
| `source` | string | Source label: greenhouse. |
| `boardSlug` | string | Greenhouse board token. |
| `boardUrl` | string | Public board URL. |
| `sourceJobId` | string, null | Public posting identity within its board. |
| `internalJobId` | string, null | Employer internal job identity when supplied. |
| `requisitionId` | string, null | Published requisition identifier. |
| `title` | string, null | Published role title. |
| `companyName` | string, null | Employer name when supplied. |
| `jobUrl` | string, null | Public job posting URL. |
| `applyUrl` | string, null | Public application link; no application is submitted. |
| `location` | string, null | Primary published location label. |
| `locations` | array | Available location labels. |
| `department` | string, null | First available department. |
| `departments` | array | Available department objects. |
| `offices` | array | Available office objects. |
| `metadata` | array | Employer-provided metadata. |
| `country` | string, null | Available country information; may be null. |
| `employmentType` | string, null | Available employment type; may be null. |
| `team` | string, null | Available team; may be null. |
| `workplaceType` | string, null | Available workplace arrangement; may be null. |
| `isRemote` | boolean, null | Available remote flag; may be null. |
| `postedAt` | string, null | Published timestamp when supplied. |
| `updatedAt` | string, null | Last update timestamp when supplied. |
| `applicationDeadline` | string, null | Application deadline when supplied; may be null. |
| `language` | string, null | Posting language when supplied. |
| `descriptionHtml` | string, null | Optional job description as HTML. |
| `descriptionText` | string, null | Optional readable job description. |
| `compensation` | object, null | Available structured compensation; may be null. |
| `sourceData` | object, null | Not populated; null. |
| `scrapedAt` | string | Collection timestamp. |

Optional values can be null or empty and are not guaranteed for every job. `includeContent` controls descriptions and available department/office detail. `SUMMARY` and `ERRORS` are separate records in the run key-value store. Require truthful coverage before comparing snapshots; a limited complete run does not mean every source posting was collected.
