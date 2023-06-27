import os
import sys
import scrapy
import logging
from scraping_news.utils.source_help import SourceHelp
from scraping_news.utils.services.noticia_service import NoticiaService


class NewsTextSpider(scrapy.Spider):
    name = "news_text"
    gravar_bd = False
    logger = logging.getLogger(__name__)

    def start_requests(self):
        ns = NoticiaService()
        urls = ns.consultar_link_extracao()

        self.logger.info('Quantidade de notícias: ' + str(len(urls)))

        for url in urls:
            sh = SourceHelp()
            src = sh.get_model_by_url(url)
            yield scrapy.Request(
                url,
                src.parse_news,
                meta={
                    'titulo': '',
                    'link': url
                }
            )

    @staticmethod
    def closed(reason):
        # Subir arquivo para o bucket
        args = sys.argv

        output_file_index = args.index('-O')
        output_file = args[output_file_index + 1]
        filepath = os.path.abspath(output_file)

        # TODO  Fazer serviço para fazer o upload do arquivo no S3
        #       Se basear no código abaixo e no código do poupay do twitter
        #       Método vai receber o filepath e filepath que vai ser gravado no bucket,
        #       pegar o bucket_name por variável de ambiente

        '''
        import boto3
        bucket_name = 'nome-do-seu-bucket'
        s3_key = 'extracao/extracao.csv'

        s3 = boto3.client('s3')
        s3.upload_file(filepath, bucket_name, s3_key)
        '''
