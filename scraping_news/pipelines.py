from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scraping_news.utils.services.noticia_service import NoticiaService


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
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if spider.gravar_bd:
            adapter = ItemAdapter(item)
            ns = NoticiaService()
            ns.inserir_noticia(adapter["link"])
