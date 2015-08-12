# encoding: utf-8
import re
from bs4 import BeautifulSoup
import threading
import urllib

class Sp(object):
    def __init__(self, url, key, Queue, deep=2):
        threading.Thread.__init__(self)
        self.url = url
        self.deep = deep
        self.key = key
        self.queue = Queue
        self.sq = Sqlite()
    def run(self):
        self.queue.add_job(self.url, self.deep)
        
    def get_soup(self, url):
        try:
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html)
        except urllib.HTTPError, e:
            logging.critical("Get html failed %s %s" % (e.code, e.read()))
        return soup

    def get_url(self, start_url, deep):
        urls = []
        soup = self.get_soup(url)
        links = soup.find_all('a')
        if_has_key(soup.get_text())
        deep = deep - 1
        for link in links:
            _url = link.get('href')
            if re.match('^(javascript|:;|#)', _url) or _url is None \
                or re.match('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso\
                             |pdf|txt|db)$', _url):
                continue
            if re.match('^(http|https)', _url):
                if sq.find_url(_url) or deep < 0:
                    continue
                else:
                    sq.insert_url(url)
                    self.queue.add_job(get_url, _url, deep)

    def if_has_key(self, soup_text):
        findpage = soup_text.encode('utf-8')
        if re.findall(self.key, findpage) != []:
            insert_page(self.key, find_page)


                
