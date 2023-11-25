import logging
from scraping_news.utils.sources.source_cnn import SourceCnn
from scraping_news.utils.sources.source_aos_fatos import SourceAosFatos
from scraping_news.utils.sources.source_base import SourceBase
from scraping_news.utils.sources.source_g1 import SourceG1


class SourceHelp:
    loger = None

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_model(self, name: str) -> SourceBase:
        fonte = name.lower()
        match fonte:
            case 'cnn':
                self.logger.info('Fonte selecionada: CNN')
                return SourceCnn()
            case 'aos_fatos':
                self.logger.info('Fonte selecionada: Aos Fatos')
                return SourceAosFatos()
            case 'g1':
                self.logger.info('Fonte selecionada: G1')
                return SourceG1()
            case _:
                self.logger.warning('Fonte informada não reconhecida')
                raise Exception('Fonte informada não reconhecida')

    def get_model_by_url(self, url: str) -> SourceBase | None:
        if url.find('cnn') > -1:
            self.logger.info(url + ' | Fonte selecionada: CNN')
            return SourceCnn()
        if url.find('aosfatos') > -1:
            self.logger.info(url + ' | Fonte selecionada: Aos Fatos')
            return SourceAosFatos()
        if url.find('g1') > -1:
            self.logger.info(url + ' | Fonte selecionada: G1')
            return SourceG1()
        else:
            self.logger.warning(url + ' | Fonte informada não reconhecida')
            return None
