# encoding: utf-8
import re
from bs4 import BeautifulSoup
import urllib2

class Sp(object):
    def __init__(self, url, deep=2):
        self.url = url
        self.deep = deep

    def get_soup(self, url):
        try:
            html = urllib2.urlopen(url).read()
            soup = BeautifulSoup(html)
        except urllib2.HTTPError, e:
            logging.critical("Get html failed %s %s" % (e.code, e.read()))
        return soup

    def get_url(self, start_url):
        urls = []
        soup = self.get_soup(url)
        links = soup.find_all('a')
        for link in links:
            _url = link.get('href')
            if re.match('^(javascript|:;|#)', _url) or _url is None \
                or re.match('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso\
                             |pdf|txt|db)$', _url):
                continue
            if re.match('^(http|https)', _url):
                urls.append(_url)
        return urls


                
