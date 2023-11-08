import scrapy
from scraping_news.utils.sources.source_base import SourceBase
from scraping_news.items import NewsItem


class SourceG1(SourceBase):

    @property
    def name(self):
        return "g1"

    @property
    def base_url(self):
        return 'https://g1.globo.com'

    @property
    def url_mtd(self):
        return 'date'

    @property
    def pg_lgc(self):
        return None

    def parse(self, response):
        for news in response.css('.feed-post-link'):
            titulo = news.css('p::text').get()
            link = news.css('.feed-post-link::attr(href)').get()

            yield scrapy.Request(
                link,
                callback=self.parse_news,
                meta={
                    'titulo': titulo,
                    'link': link
                }
            )

    def parse_news(self, response):
        titulo = response.meta.get('titulo')
        link = response.meta.get('link')

        if len(response.css('.playlist')) > 0 or response.css('.blink::text').get() == 'Ao vivo' or link.find('ge.globo.com') > -1:
            return None

        fonte = self.name
        data = response.css('.content-publication-data__updated time::attr(datetime)').get()
        autoria = "".join(response.css('.content-publication-data__from::text, .multi_signatures::text').extract()).strip()

        texto_noticia = response.css('.content-text__container::text, .content-text__container strong::text, .content-text__container a::text, blockquote::text').extract()
        texto_unido = "".join(texto_noticia).strip()

        return NewsItem(titulo, texto_unido, autoria, link, fonte, data)
