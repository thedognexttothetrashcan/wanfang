# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

import pymysql
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings



class WanfangPeriodicalPipeline(object):

    def __init__(self):
        settings = get_project_settings()
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.pwd = settings["DB_PWD"]
        self.name = settings["DB_NAME"]
        self.charset = settings["DB_CHARSET"]

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.pwd,
                                    database=self.name,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    def colose_spider(self, spider):
        self.conn.close()
        self.cursor.close()
    def process_item(self, item, spider):
        '''
        字段：
        id,perio_title,hostunit_name,language,issn,cn,release_cycle,affectoi,article_num,funded_papers,cite_num,download_num,core_perio,trans_title,crawl_time

        :param item:
        :param spider:
        :return:
        '''
        # 查重：

        print('**********************@***********************')
        sql_read = """select perio_id from periodical_list_new where perio_id='%s'""" % item['perio_id']
        print(sql_read)
        self.cursor.execute(sql_read.replace("'None'", pymysql.NULL))
        print('SQL执行-------------------------')
        repetition = self.cursor.fetchone()
        print('SQL查询***********************************')
        if repetition:
            spider.logger.info(msg='此条重复抓取，没有存入数据库')
        else:
            sql_insert = """insert into periodical_list_new(\
            perio_id,perio_title,hostunit_name,language,\
            issn,cn,cn_short,release_cycle,affectoi,article_num,\
            funded_num,cite_num,download_num,core_perio,trans_title,crawl_time)\
            values('%s','%s','%s','%s','%s','%s','%s','%s',%s,%s,%s,%s,%s,'%s','%s','%s')""" % \
            (
            pymysql.escape_string(item['perio_id']) if item['perio_id'] is not None else None,
            pymysql.escape_string(item['perio_title']) if item['perio_title'] is not None else None,
            pymysql.escape_string(item['hostunit_name']) if item['hostunit_name'] is not None else None,
            pymysql.escape_string(item['language']) if item['language'] is not None else None,
            pymysql.escape_string(item['issn']) if item['issn'] is not None else None,
            pymysql.escape_string(item['cn']) if item['cn'] is not None else None,
            pymysql.escape_string(item['cn_short']) if item['cn_short'] is not None else None,
            pymysql.escape_string(item['release_cycle']) if item['release_cycle'] is not None else None,
            item['affectoi'],
            item['article_num'],
            item['funded_num'],
            item['cite_num'],
            item['download_num'],
            pymysql.escape_string(item['core_perio']) if item['core_perio'] is not None else None,
            pymysql.escape_string(item['trans_title']) if item['trans_title'] is not None else None,
            item['crawl_time'],
            )
            try:
                self.cursor.execute(sql_insert.replace("'None'", pymysql.NULL))
                self.conn.commit()
                a = 0
                a += 1
                print('成功存入%d条数据' % a)
            except Exception as e:
                spider.logger.info(sql_insert)
                self.conn.rollback()
                print(sql_insert)
                spider.logger.error(msg='存入数据库失败 %s' % e)
        return item

class MongoproPipeline(object):
    # bind 127.0.0.1   注释这个选项即可
    def open_spider(self, spider):
        # 链接MongoDB服务器
        self.client = MongoClient('localhost', 27017)
        print('成功连接MongoDB------------------------------')
        # 选择数据库
        db = self.client.wanfang
        # 选择集合
        self.conn = db.proid

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        d = dict(item)
        self.conn.insert_one(d)
        num = 0
        num += 1
        spider.logger.info('成功存入%d条数据' % num)
        return item
