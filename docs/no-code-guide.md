# Collect Greenhouse jobs without code

Open [Greenhouse Jobs Scraper](https://apify.com/datascraperes/greenhouse-jobs-scraper?fpr=edudata), choose Input and paste company board URLs or tokens into `boardUrls`. For a first run use one board and a total limit of three jobs, as in [sample input](../data/sample-input.json).

Review the Pricing tab, set the maximum charge and timeout in Console, then click Start. Once finished, open the Dataset to inspect and export JSON or CSV. Inspect `SUMMARY` and `ERRORS` in the key-value store: a run can preserve useful jobs while a requested board is unavailable. Missing SUMMARY means completeness cannot be confirmed.

Descriptions are enabled by default through `includeContent`. Departments and offices are included when available. The Actor collects specified boards; it does not discover every company using Greenhouse.
