import scrapy
from scraping_news.items import NewsItem
from scraping_news.utils.sources.source_base import SourceBase


class SourceAosFatos(SourceBase):

    @property
    def name(self):
        return "aos-fatos"

    @property
    def base_url(self):
        return 'https://www.aosfatos.org/noticias/checamos/falso/'

    @property
    def url_mtd(self):
        return 'page'

    @property
    def pg_lgc(self):
        return '?page=@@'

    def parse(self, response):
        for news in response.css('.entry-content'):
            titulo = news.css('.entry-item-card-title p::text').get()
            link = 'https://www.aosfatos.org' + news.css('.entry-content::attr(href)').get()

            yield scrapy.Request(
                link,
                callback=self.parse_news,
                meta={
                    'titulo': titulo,
                    'link': link
                }
            )

    def parse_news(self, response):
        fonte = self.name

        titulo = response.meta.get('titulo')
        link = response.meta.get('link')
        data = response.css('.publish-date::text').get().strip().replace('\n', '').replace('       ', '')
        autoria = response.css('.author::text').get()

        texto_noticia = response.css('.entry-content p').extract()
        texto_unido = " ".join(texto_noticia)

        return NewsItem(titulo, texto_unido, autoria, link, fonte, data)
