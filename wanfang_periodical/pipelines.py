# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

import pymysql
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
        return item


