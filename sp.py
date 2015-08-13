# encoding: utf-8
import re
from bs4 import BeautifulSoup
import threading
import urllib
import logging
from sqlite import Sqlite

class Sp(object):
    def __init__(self, url, key, Queue, dbfile, deep=2):
        #threading.Thread.__init__(self)
        self.url = url
        self.deep = deep
        self.key = key
        self.dbfile = dbfile
        self.queue = Queue
        self.sq = Sqlite(dbfile)

    def run(self):
        print 'job start'
        self.queue.add_job(self.get_url, self.url, self.deep)
        self.queue.wait_for_complete()

    def get_soup(self, url):
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        print soup.title
        return soup

    def get_url(self, start, kwargs):
        start_url, deep = start
        urls = []
        soup = self.get_soup(start_url)
        links = soup.find_all('a')
        self.if_has_key(soup.get_text())
        deep = deep - 1
        for link in links:
            _url = link.get('href')
            print _url
            if re.match('^(javascript|:;|#)', _url) or _url is None \
                or re.match('.(jpg|png|bmp|mp3|wma|wmv|gz|zip|rar|iso\
                             |pdf|txt|db)$', _url):
                continue
            if re.match('^(http|https)', _url):
                if sq.find_url(_url) or deep < 0:
                    continue
                else:
                    print _url
                    sq.insert_url(_url)
                    self.queue.add_job(get_url, _url, deep)

    def if_has_key(self, soup_text):
        findpage = soup_text.encode('utf-8')
        if self.key is None:
            self.sq.insert_page(None, findpage)
        if re.findall(self.key, findpage) != []:
            self.sq.insert_page(self.key, find_page)


                
