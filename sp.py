#! /usr/bin/env python
#encodig: utf-8

import logging
import sys
import getopt

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
        options, args = getopt.getopt(argvs[1:], "hu:d:l:", ['help', 'thread=', 'dbfile=', 'selftest'])
    except Exception, e:
        sys.exit()

    for opt, values in options:
        if opt in ['-h', '--help']:
            help_message()


if  __name__ == '__main__':
    args_process(sys.argv)
