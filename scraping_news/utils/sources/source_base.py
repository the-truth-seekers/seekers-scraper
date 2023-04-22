from scraping_news.utils.others.date_help import format_datestr_to_date, format_date_to_str
from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class SourceBase(ABC):
    DEFAULT_DAYS=7
    URL_BASE_WEB_ARCHIVE = 'https://web.archive.org/web/'

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def base_url(self):
        pass

    @abstractmethod
    def parse(self, response):
        pass

    @abstractmethod
    def parse_news(self, response):
        pass

    def get_urls(self, start_date=None, end_date=None):
        start = format_datestr_to_date(start_date) if (start_date != None) \
            else (datetime.now() - timedelta(days=self.DEFAULT_DAYS))

        end = format_datestr_to_date(end_date) if (end_date != None) \
            else (datetime.now() - timedelta(days=1))

        retorno = []

        dt_aux = start

        while dt_aux <= end:
            date_str = format_date_to_str(dt_aux)
            retorno.append(self.build_url(date_str))
            dt_aux = (dt_aux + timedelta(days=1))

        retorno.append(self.base_url)

        return retorno

    def build_url(self, date_string: str):
        return self.URL_BASE_WEB_ARCHIVE + date_string + '/' + self.base_url