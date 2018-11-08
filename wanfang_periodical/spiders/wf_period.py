# -*- coding: utf-8 -*-
import datetime
import json
import re
from collections import OrderedDict
from lxml import etree

import scrapy
import requests
from wanfang_periodical.items import WanfangPeriodicalItem
class WfPeriodSpider(scrapy.Spider):
    name = 'wf_period'
    allowed_domains = ['www.wanfangdata.com.cn']
    start_urls = ['http://www.wanfangdata.com.cn/']

    def start_requests(self):
        url = 'http://www.wanfangdata.com.cn/perio/page.do'
        url_cnTree = 'http://www.wanfangdata.com.cn/perio/cnTree.do'
        self.headers = {
            'Referer': 'http://www.wanfangdata.com.cn',
            'Origin': 'http://www.wanfangdata.com.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }
        cnTree_form = {
            'fromData': 'WF',
        }
        # yield scrapy.FormRequest(url=url, method='POST', headers=self.headers, formdata=form_data,
        #                          callback=self.parse, dont_filter=True,
        #                          meta={'paramStrs': paramStrs, 'pageNum': pageNum, 'name': name})

        yield scrapy.FormRequest(url=url_cnTree, method='POST', headers=self.headers, formdata=cnTree_form,callback=self.parse)

    def parse(self, response):
        obj = json.loads(response.text)
        url_page = 'http://www.wanfangdata.com.cn/perio/page.do'
        page_size = 3
        for category in obj[:-1]:
            page_count = category['count']//page_size + 1
            for i in range(page_count):
                i += 1
                post_form = {
                    'page': str(i),
                    'pageSize': str(page_size),
                    'selectOrder': 'affectoi',
                    'fmList': category['id'],
                    'fromData': 'WF',
                }

                # print(i)
                # print('#'*90)
                yield scrapy.FormRequest(url=url_page, method='POST', headers=self.headers, formdata=post_form,callback=self.parse_page,meta={'page_num':i,'page_size':page_size})
                break

    def parse_page(self, response):
        page_num = response.meta['page_num']
        obj = json.loads(response.text)

        # with open('./d.txt','a') as f:
        #     f.write(response.text+',\n\n')
        # exit()

        for pageRow in obj['pageRow']:
            item = WanfangPeriodicalItem()
            item['perio_id'] = pageRow['perio_id']  # 期刊id参数
            item['perio_title'] = pageRow['perio_id']  # 期刊名称
            item['hostunit_name'] = pageRow['hostunit_name']  # 主办单位 列表，以&隔开
            item['language'] = pageRow['language']  # 语种
            item['issn'] = pageRow['issn']  # 国际刊号
            item['cn'] = pageRow['cn']  # 国内刊号
            item['cn_short'] = pageRow['cn_short']  # 国内刊号/后面的字符
            item['release_cycle'] = pageRow['release_cycle']  # 出版周期
            item['affectoi'] = pageRow['affectoi']  # 影响因子
            item['article_num'] = pageRow['article_num']  # 载文量

            # item['funded_num'] = pageRow['funded_num']  # 基金论文量

            item['cite_num'] = pageRow['cite_num']  # 被引量
            item['download_num'] = pageRow['download_num']  # 下载量
            item['core_perio'] = pageRow['core_perio']  # 期刊 标签 列表，以&隔开
            item['trans_title'] = pageRow['trans_title']  # 期刊外文名称
            now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 当前时刻
            item['crawl_time'] = now_time  # 采集时间
            url_detail = 'http://www.wanfangdata.com.cn/perio/detail.do?perio_id=%s' % pageRow['perio_id']
            content = requests.get(url=url_detail,headers=self.headers).text
            tree = etree.HTML(content)
            funds = tree.xpath('//div[@class="top-rt"]/div[3]/text()')
            funds_num = funds[0]
            a = re.sub(r'\D','',funds_num)
            item['funded_num'] = int(a)









