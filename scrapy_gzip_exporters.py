import gzip
from scrapy.exporters import (
    JsonLinesItemExporter,
    JsonItemExporter,
    XmlItemExporter,
    CsvItemExporter,
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
class GzipItemExporterMixin(object):

    def __init__(self, file, **kwargs):
        self.gzfile = gzip.GzipFile(fileobj=file)
        super(GzipItemExporterMixin, self).__init__(self.gzfile, **kwargs)

    def finish_exporting(self):
        super(GzipItemExporterMixin, self).finish_exporting()
        self.gzfile.close()


class JsonLinesGzipItemExporter(GzipItemExporterMixin, JsonLinesItemExporter):
    pass


class JsonGzipItemExporter(GzipItemExporterMixin, JsonItemExporter):
    pass


class XmlGzipItemExporter(GzipItemExporterMixin, XmlItemExporter):
    pass


class CsvGzipItemExporter(GzipItemExporterMixin, CsvItemExporter):
    pass
