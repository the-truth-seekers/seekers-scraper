import scrapy
import asyncio
from scraping_news.utils.source_help import SourceHelp
from scraping_news.utils.others.validations import valid_input_date
from scraping_news.utils.others.validations import valid_int
from scraping_news.utils.others.constants import FONTES


class NewsSpider(scrapy.Spider):
    name = "news"

    def start_requests(self):
        parametros = {
            'p_fonte': getattr(self, 'fonte', None),
            'p_start_date': getattr(self, 'start_date', None),
            'p_end_date': getattr(self, 'end_date', None),
            'p_num_pages': getattr(self, 'num_pages', None),
        }

        self.criticar(parametros)

        sh = SourceHelp()
        src = sh.get_model(parametros['p_fonte'])

        urls = src.get_urls(
            start_date=parametros['p_start_date'],
            end_date=parametros['p_end_date'],
            num_pages=parametros['p_num_pages']
        )

        for url in urls:
            yield scrapy.Request(url, src.parse)

    @staticmethod
    def criticar(parametros):
        if parametros['p_fonte'] is None or parametros['p_fonte'] not in FONTES:
            print('fonte: Fonte informada inválida')
            raise Exception('fonte: Fonte informada inválida')

        if parametros['p_start_date'] is not None and not valid_input_date(parametros['p_start_date']):
            print("start_date: Formato de data incorreto, deve ser informado com o formato YYYY-MM-DD")
            raise Exception('start_date: Formato de data incorreto, deve ser informado com o formato YYYY-MM-DD')

        if parametros['p_end_date'] is not None and not valid_input_date(parametros['p_end_date']):
            print("end_date: Formato de data incorreto, deve ser informado com o formato YYYY-MM-DD")
            raise Exception("end_date: Formato de data incorreto, deve ser informado com o formato YYYY-MM-DD")

        if parametros['p_num_pages'] is not None and not valid_int(parametros['p_num_pages']):
            print("num_pages: Deve ser informado um valor numérico inteiro")
            raise Exception("end_date: Formato de data incorreto, deve ser informado com o formato YYYY-MM-DD")
