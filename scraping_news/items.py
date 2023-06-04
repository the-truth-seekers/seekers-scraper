from scrapy.item import Item, Field
from bs4 import BeautifulSoup


class NewsItem(Item):
    titulo = Field()
    texto_noticia = Field()
    autoria = Field()
    link = Field()
    fonte = Field()
    data = Field()

    def set_texto_noticia(self, texto):
        # Remover as tags HTML e extrair apenas o texto
        soup = BeautifulSoup(texto, 'html.parser')
        texto_limpo = soup.get_text(strip=False)
        self['texto_noticia'] = texto_limpo

    def __init__(self, titulo=None, texto_noticia=None, autoria=None, link=None, fonte=None, data=None,
                 *args, **kwargs):
        super(NewsItem, self).__init__(*args, **kwargs)
        self['titulo'] = titulo
        self['autoria'] = autoria
        self['link'] = link
        self['fonte'] = fonte
        self['data'] = data
        self.set_texto_noticia(texto_noticia)

