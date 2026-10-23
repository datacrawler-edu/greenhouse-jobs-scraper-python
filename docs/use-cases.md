# Greenhouse job data workflows

## Refresh a job directory

Run [collect_jobs.py](../examples/python/collect_jobs.py) against a known board. Use `(boardSlug, sourceJobId)` to identify postings across snapshots. Preserve the last complete snapshot when a later collection has incomplete coverage; a source failure does not mean every job has closed.

## Compare hiring across companies

Use [batch_boards.py](../examples/python/batch_boards.py) for two named boards in one run. Increase limits deliberately and review maximum charges before expanding the workload. A global limit can leave later boards unprocessed even when the limited collection is complete.

## Analyze published job descriptions

Enable `includeContent` and read `descriptionText` or `descriptionHtml`. Departments and offices are also returned when available. Extract skills or requirements downstream; this integration does not infer them.

## Export existing results

Use [export_jobs_csv.py](../examples/python/export_jobs_csv.py) with an existing Dataset ID. It exports selected columns from at most 1,000 rows and starts no collection. For descriptions and nested department and office data, export JSON instead. The CSV example prefixes formula-like values with an apostrophe for spreadsheet safety.
