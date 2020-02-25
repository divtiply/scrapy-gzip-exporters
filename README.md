# scrapy-gzip-exporters

Scrapy Item Exporters which allows export into gzip compressed feed.
Supported formats: CSV (csv.gz), XML (xml.gz), JSON (json.gz), and
JSON lines (jsonl.gz, jsonlines.gz, jl.gz).

This package also adds jsonl output format alias for JSON lines feed.


## Setup

Add the following line to your project `settings.py`:
```python
from scrapy_gzip_exporters import FEED_EXPORTERS
```

Set desired output format:
```python
FEED_FORMAT = 'csv.gz'
```

or specify it with `--output-format` (`-t`) commandline tool option:
```sh
scrapy crawl myspider -o outfile.csv.gz -t csv.gz
```

## Tip

To get CSV encoded in UTF-8 variant understood by Microsoft Excel, set
```python
FEED_EXPORT_ENCODING = 'utf-8-sig'
```
