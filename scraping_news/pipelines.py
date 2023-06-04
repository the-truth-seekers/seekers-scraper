from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class ScrapingNewsPipeline:
    def process_item(self, item, spider):
        return item


class DuplicatesPipeline:
    def __init__(self):
        self.links_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter["link"] in self.links_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.links_seen.add(adapter["link"])
            return item


class AzurePipeline:
    def process_item(self, item, spider):
        if spider.gravar_bd:
            # TODO Gravação na base de dados da Azure
            print()

