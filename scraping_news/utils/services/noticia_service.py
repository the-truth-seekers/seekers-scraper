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

    @staticmethod
    def consultar_link_extracao():
        query = 'SP_CONSULTAR_LINKS_EXTRACAO'

        bd_aux = BdAux()
        rows = bd_aux.get_query(query)
        bd_aux.desconectar()

        links = []

        for r in rows:
            links.append(r[0])

        return links
