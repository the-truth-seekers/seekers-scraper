import os
import sys
import scrapy
import logging

from scraping_news.utils.aws.s3_aux import send_file_to_bucket
from scraping_news.utils.source_help import SourceHelp
from scraping_news.utils.services.noticia_service import NoticiaService


class NewsTextSpider(scrapy.Spider):
    name = "news_text"
    gravar_bd = False
    logger = logging.getLogger(__name__)
    bucket_name = None
    output_file = None

    def start_requests(self):
        args = sys.argv
        ns = NoticiaService()
        urls = ns.consultar_link_extracao()

        output_file_index = args.index('-O')
        self.bucket_name = getattr(self, 'bucket_name', None)

        self.criticar(output_file_index, self.bucket_name)

        self.output_file = args[output_file_index + 1]

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

    def closed(self, reason):
        filepath = os.path.abspath(self.output_file)
        send_file_to_bucket(self.bucket_name, filepath, 'extracao/extracao.csv')
        self.logger.info("Enviado para o bucket: " + self.bucket_name)

    @staticmethod
    def criticar(output_file_index, bucket_name):
        if output_file_index < 0:
            raise Exception('output_file: deve ser indicado um arquivo de saída no comando')

        if bucket_name is None:
            raise Exception('bucket_name: deve ser indicado o parâmetro bucket_name')
