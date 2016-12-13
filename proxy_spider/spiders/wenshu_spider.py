# -*- coding:utf-8 -*-
__author__ = 'Mr.Tian'

import scrapy

from ..items import NodeItem, WenshuItem
import datetime

DEBUG=True
class WenshuSpider(scrapy.Spider):
    name = "wenshu_spider"
    allowed_domains = [
        "wenshu.court.gov.cn"
    ]

    # start_urls = [
    #     "http://ip84.com/dl"
    # ]

    custom_settings = {
        'LOG_FILE': 'log/wenshu.log'
    }

    def start_requests(self):
        pass
        # if DEBUG:
        #     for i in range(1, 4):
        #         for j in range(1, 10):   # page
        #             url = "http://www.ip3366.net/free/?stype=%s&page=%s" % (i, j)
        #             yield scrapy.Request(url, self.parse)
        # else:
        #     for i in range(1, 21):
        #         formdata = {
        #             "Param":"法院层级:最高法院",
        #             "Index":i,
        #             "Page":20,
        #             "Order":"法院层级",
        #             "Direction":"asc"
        #             }
        #         url = "http://wenshu.court.gov.cn/List/ListContent"
        #         yield scrapy.FormRequest(url, formdata=formdata, callback=self.parse,meta={'param': formdata['Param']})

    def parse(self, response):
        print "parsing ",response.body
        for item in json.loads(response.body):
            if item.get('Count'):
                node_item = NodeItem()
                node_item['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                node_item['param'] = response['meta']['param']
                node_item['count'] = item.get('Count')
                yield node_item
            else:
                abstract_item = WenshuItem()
                abstract_item['abstract'] = item['裁判要旨段原文']
                abstract_item['type'] = item['案件类型']
                abstract_item['time'] = item['裁判日期']
                abstract_item['name'] = item['案件名称']
                abstract_item['id'] = item['文书ID']
                abstract_item['procedure'] = item['审判程序']
                abstract_item['caseid'] = item['案号']
                abstract_item['courtname'] = item['法院名称']
                yield abstract_item
