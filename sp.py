#! /usr/bin/env python
#encodig: utf-8

import logging
import sys
import getopt


class Spider(object):
    def __init__(self, url, deep, thread=10, dbfile='./spyder.log', key=None, detal=9):
        self.url = url
        self.deep = deep
        self.thread = thread
        self.dbfile = dbfile
        self.key = key
        self.detal = detal

    def 

def help_message():
    print '\tspider.py usage:'
    print '\t\t-h, --help: print help messages.'
    print '\t\t-u: url to start.'
    print '\t\t-d: how deep of the spider.'
    print '\t\t--thread: size of threading pool.'
    print '\t\t--dbfile: db file to save results.'
    print '\t\t--key: keywords of the page, optional parameter, default is all the page.'
    print '\t\t-l: loglevel 1-5 1:debug, 2:info, 3:warning, 4:error, 5:critical.'
    print '\t\t--selftest: self test, optional.'

def args_process(argvs):
    try:
        options, args = getopt.getopt(argvs[1:], "hu:d:l:", ['help',
                                      'thread=', 'dbfile=', 'selftest'])
    except Exception, e:
        sys.exit()
    op_get = {'detal': 9, 'thread': 10, 'dbfile': './spyder.log',
              'key': None, 'selftest': False}
    for opt, values in options:
        if opt in ['-h', '--help']:
            help_message()
            return None
        elif opt == '-u':
            op_get['url'] = values
        elif opt == '-d':
            op_get['deep'] = values
        elif opt == '-l':
            op_get['detal'] = values
        elif opt == '--thread':
            op_get['thread'] = values
        elif opt == '--dbfile':
            op_get['dbfile'] = values
        elif opt == '--key':
            op_get['key'] = values
        elif opt == 'selftest':
            op_get['selftest'] = True
    if not op_get.has_key('url'):
        raise RuntimeError('Please provide url!')
    if not op_get.has_key('deep'):
        raise RuntimeError('Please provide deep to spyder')
    return op_get

if  __name__ == '__main__':
    option = args_process(sys.argv)
    if option is not None:
        spider = Spider(option['url'], option['deep'], option['thread'],
                        option['dbfile'], option['key'], option['detal'])
        spider.start()
