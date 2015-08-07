# !/usr/bin/env python
# encoding: utf-8

import sqlite3
import logging

class Sqlite(object):
    
    def __init__(self, table, key):
        self.table = table
        self.key = key

    def sql_connect(self):
        try:
            self.sqlite_conn = sqlite3.connect(self.table)
        except sqlite3.Error, e:
            logging.warning('Connect to %s failed! Reason: %s' % (self.table, e.args[0])
            raise e.args[0]
        self.sqlite_cursor = self.sqlite_conn.cursor()
        sql_del = 'DROP TABLE IF EXISTS sp_test;'
        try:
            self.sqlite_cursor.execute(sql_del)
        except sqlite3.Error, e:
            logging.warning('Delete table failed! %s' % e.args[0])
            raise e.args[0]
        self.sqlite_conn.commit()

        sql_add = 'CREATE TABLE sp_test(id INTEGER PRIMARY KEY, key\
                   VARCHAR(128), page TEXT);'
        try:
            self.sqlite_cursor.execute(sql_add)
        except sqlite3.Error, e:
            logging.warning('Create table falied! Reason: %s' % e.args[0])
            raise e.args[0]
        self.sqlite_conn.commit()

    def sql_page(self, key, page):
        sql_insert = 'INSERT INTO sp_test(key, page) values(%s, %s);' % (key, page)
        try:
            self.sqlite_cursor.execute(sql_insert)
        except sqlite3.Error, e:
            logging.warning('Insert page date falied! Reason: %s' % e.args[0])
            raise e.args[0]
        self.sqlite_conn.commit()

    def sql_close(self):
        try:
            self.sqlite_conn.close()
        except sqlite3.Error, e:
            logging.warning('Close connection failed! Reason: %s' % e.args[0])
            raise e.args[0]
    
