from scraping_news.utils.bd.bd_aux import BdAux


class NoticiaService:
    def __init__(self):
        pass

    @staticmethod
    def inserir_noticia(link):
        query = 'EXEC SP_INSERIR_NOTICIA ?'

        bd_aux = BdAux()
        bd_aux.executar_query(query, link)
        bd_aux.desconectar()
