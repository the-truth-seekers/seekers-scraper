import scrapy
from scraping_news.utils.sources.source_base import SourceBase


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

        titulo = response.meta.get('titulo')
        link = response.meta.get('link')
        data = response.css('.post__data::text').get()
        autores = ''

        for body in response.css('body'):
            autoria = response.css('.author__group a::text')

            if (len(autoria) > 0):
                for autor in autoria:
                    nomeAutor = autor.get()

                    if autores == '':
                        autores = nomeAutor
                    else:
                        autores = autores + ' | ' + nomeAutor
            else:
                possuiAutor = len(response.css('.author__first__line span')) > 0
                autores = response.css('.author__first__line span::text').get() if possuiAutor else 'Sem Autor'

        return {
            'titulo': titulo,
            'autoria': autores,
            'link': link,
            'fonte': fonte,
            'data': data
        }
