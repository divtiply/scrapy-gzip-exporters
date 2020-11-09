import gzip

from scrapy.exporters import (
    CsvItemExporter,
    JsonItemExporter,
    JsonLinesItemExporter,
    XmlItemExporter,
)

FEED_EXPORTERS = {
    # "jsonl" is widely recognized JSON lines file extension
    'jsonl': 'scrapy.exporters.JsonLinesItemExporter',
    'jsonl.gz': __name__ + '.JsonLinesGzipItemExporter',
    'json.gz': __name__ + '.JsonGzipItemExporter',
    'jsonlines.gz': __name__ + '.JsonLinesGzipItemExporter',
    'jl.gz': __name__ + '.JsonLinesGzipItemExporter',
    'csv.gz': __name__ + '.CsvGzipItemExporter',
    'xml.gz': __name__ + '.XmlGzipItemExporter',
}


# Derived from https://github.com/scrapy/scrapy/issues/2174
class GzipMixin(object):
    def __init__(self, file, **kwargs):
        self.gzfile = gzip.GzipFile(fileobj=file)
        super(GzipMixin, self).__init__(self.gzfile, **kwargs)

    def finish_exporting(self):
        super(GzipMixin, self).finish_exporting()
        self.gzfile.close()


class JsonLinesGzipItemExporter(GzipMixin, JsonLinesItemExporter):
    pass


class JsonGzipItemExporter(GzipMixin, JsonItemExporter):
    pass


class XmlGzipItemExporter(GzipMixin, XmlItemExporter):
    pass


class CsvGzipItemExporter(GzipMixin, CsvItemExporter):
    pass
