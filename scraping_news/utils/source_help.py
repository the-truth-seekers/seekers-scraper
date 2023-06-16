import logging
from scraping_news.utils.sources.source_cnn import SourceCnn
from scraping_news.utils.sources.source_aos_fatos import SourceAosFatos
from scraping_news.utils.sources.source_base import SourceBase


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
            case _:
                self.logger.error('Fonte informada inválida')
                raise Exception('Fonte informada inválida')
