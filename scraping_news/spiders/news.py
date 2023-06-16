import scrapy
import logging
from scraping_news.utils.source_help import SourceHelp
from scraping_news.utils.others.validations import valid_input_date, valid_int, string_to_bool
from scraping_news.utils.others.constants import FONTES


class NewsSpider(scrapy.Spider):
    name = "news"
    gravar_bd = 'False'
    logger = logging.getLogger(__name__)

    def start_requests(self):

        self.gravar_bd = string_to_bool(getattr(self, 'gravar_bd', 'False'))

        if self.gravar_bd:
            self.logger.info('Gravação no banco habilitada')

        parametros = {
            'p_fonte': getattr(self, 'fonte', None),
            'p_start_date': getattr(self, 'start_date', None),
            'p_end_date': getattr(self, 'end_date', None),
            'p_start_page': getattr(self, 'start_page', None),
            'p_end_page': getattr(self, 'end_page', None),
        }

        self.criticar(parametros)
        self.set_default(parametros)

        sh = SourceHelp()
        src = sh.get_model(parametros['p_fonte'])

        urls = src.get_urls(
            start_date=parametros['p_start_date'],
            end_date=parametros['p_end_date'],
            start_page=parametros['p_start_page'],
            end_page=parametros['p_end_page'],
        )

        for url in urls:
            yield scrapy.Request(url, src.parse) 

    @staticmethod
    def criticar(parametros):
        if parametros['p_fonte'] is None or parametros['p_fonte'] not in FONTES:
            raise Exception('fonte: Fonte informada inválida')

        if parametros['p_start_date'] is not None and not valid_input_date(parametros['p_start_date']):
            raise Exception('start_date: Formato de data incorreto, deve ser informado com o formato YYYY-MM-DD')

        if parametros['p_end_date'] is not None and not valid_input_date(parametros['p_end_date']):
            raise Exception('end_date: Formato de data incorreto, deve ser informado com o formato YYYY-MM-DD')

        if parametros['p_start_page'] is not None and (not valid_int(parametros['p_start_page']
                                                                     or parametros['p_start_page'] < 1)):
            raise Exception('start_page: Deve ser informado um valor numérico inteiro, maior que 0')

        if parametros['p_end_page'] is not None and (not valid_int(parametros['p_end_page']
                                                                   or parametros['p_end_page'] < 2)):
            raise Exception('end_page: Deve ser informado um valor numérico inteiro, maior que 1')

        if parametros['p_start_page'] is not None and parametros['p_end_page'] is not None \
                and int(parametros['p_start_page']) >= int(parametros['p_end_page']):
            raise Exception('validacao: end page deve ser maior que start page')

    @staticmethod
    def set_default(parametros):
        if parametros['p_start_page'] is None:
            parametros['p_start_page'] = 1

        if parametros['p_end_page'] is None:
            parametros['p_end_page'] = 5
