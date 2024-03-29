import scrapy
from scraping_news.utils.sources.source_base import SourceBase
from scraping_news.items import NewsItem


class SourceCnn(SourceBase):

    @property
    def name(self):
        return "cnn"

    @property
    def base_url(self):
        return 'https://www.cnnbrasil.com.br/'

    @property
    def url_mtd(self):
        return 'date'

    @property
    def pg_lgc(self):
        return None

    def parse(self, response):
        for news in response.css('.home__post'):
            titulo = news.css('.home__post::attr(title)').get()
            link = news.css('.home__post::attr(href)').get()

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

        titulo = response.meta.get('titulo') or response.css('.post__title::text').get()
        titulo = titulo.strip()

        link = response.meta.get('link')
        data = response.css('.post__data::text').get()
        autores = ''

        texto_noticia = response.css('.post__content > p').extract()
        texto_unido = " ".join(texto_noticia)

        for body in response.css('body'):
            autoria = response.css('.author__group a::text')

            if len(autoria) > 0:
                for autor in autoria:
                    nome_autor = autor.get()

                    if autores == '':
                        autores = nome_autor
                    else:
                        autores = autores + ' | ' + nome_autor
            else:
                possui_autor = len(response.css('.author__first__line span')) > 0
                autores = response.css('.author__first__line span::text').get() if possui_autor else 'Sem Autor'

        return NewsItem(titulo, texto_unido, autores, link, fonte, data)
