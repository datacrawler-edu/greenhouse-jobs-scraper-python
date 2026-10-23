# Greenhouse jobs API with cURL

Run from the repository root in a POSIX shell with `APIFY_API_TOKEN` set. This starts a chargeable hosted run: five-minute server timeout, $0.05 maximum Actor charge, and three-job sample input. Platform charges may apply separately.

```bash
curl --fail-with-body --max-time 45 -H "Authorization: Bearer $APIFY_API_TOKEN" -H "Content-Type: application/json" --data-binary @data/sample-input.json 'https://api.apify.com/v2/acts/datascraperes~greenhouse-jobs-scraper/runs?build=latest&timeout=300&maxTotalChargeUsd=0.05' --output greenhouse-start.json
```

Read `data.id`, `data.defaultDatasetId` and `data.defaultKeyValueStoreId` from the response. Replace the identifiers below. Do not repeat the POST automatically if its acknowledgement is lost; first inspect Actor runs in Console.

```bash
curl --fail-with-body --max-time 30 -H "Authorization: Bearer $APIFY_API_TOKEN" 'https://api.apify.com/v2/actor-runs/RUN_ID'
```

Wait for a terminal status (`SUCCEEDED`, `FAILED`, `ABORTED` or `TIMED-OUT`). The server timeout bounds collection if you stop checking status. Use Python or JavaScript for automated polling and watchdog behavior. Download available rows and inspect the summary:

```bash
curl --fail-with-body --max-time 30 -H "Authorization: Bearer $APIFY_API_TOKEN" 'https://api.apify.com/v2/datasets/DATASET_ID/items?clean=true&format=json&limit=100' --output greenhouse-jobs.json
curl --fail-with-body --max-time 30 -H "Authorization: Bearer $APIFY_API_TOKEN" 'https://api.apify.com/v2/key-value-stores/KEY_VALUE_STORE_ID/records/SUMMARY'
```

Require `SUMMARY.complete` before treating the requested limited collection as complete. Missing summary means unknown coverage. Reading an existing Dataset starts no new run or job-result events.
