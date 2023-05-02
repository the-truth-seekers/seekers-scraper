from scraping_news.utils.sources.source_cnn import SourceCnn
from scraping_news.utils.sources.source_aos_fatos import SourceAosFatos
from scraping_news.utils.sources.source_base import SourceBase

class SourceHelp():
    def __init__(self):
        pass

    def get_model(self, name: str) -> SourceBase:
        fonte = name.lower()
        match fonte:
            case 'cnn':
                print('Fonte selecionada: CNN')
                return SourceCnn()
            case 'aos_fatos':
                print('Fonte selecionada: Aos Fatos')
                return SourceAosFatos()
            case _:
                print('Fonte informada inválida')
                raise Exception()
