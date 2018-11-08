# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WanfangPeriodicalItem(scrapy.Item):
    perio_id = scrapy.Field()  # 期刊id参数
    perio_title = scrapy.Field()  # 期刊名称
    hostunit_name = scrapy.Field()  # 主办单位 列表，以&隔开
    language = scrapy.Field()  # 语种
    issn = scrapy.Field()  # 国际刊号
    cn = scrapy.Field()  # 国内刊号
    cn_short = scrapy.Field()  # 国内刊号/后面的字符
    release_cycle = scrapy.Field()  # 出版周期
    affectoi = scrapy.Field()  # 影响因子
    article_num = scrapy.Field()  # 载文量
    funded_num = scrapy.Field()  # 基金论文量
    cite_num = scrapy.Field()  # 被引量
    download_num = scrapy.Field()  # 下载量
    core_perio = scrapy.Field()  # 期刊 标签 列表，以&隔开
    trans_title = scrapy.Field()  # 期刊外文名称
    crawl_time = scrapy.Field()  # 采集时间


