# -*- coding:utf-8 -*-
__author__ = 'Mr.Tian'

import scrapy

from ..items import NodeItem, WenshuItem
import datetime
import urllib2
from urllib import urlencode
import logging

DEBUG=False
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
    
        for i in range(1, 2):
            formdata = {
                "Param":"法院层级:最高法院",
                "Index":"%d"%i,
                "Page":"20",
                "Order":"法院层级",
                "Direction":"asc",
                }
            encodedata = urlencode(formdata)
            url = "http://wenshu.court.gov.cn/List/ListContent"
            headers = {"Content-Type": "application/x-www-form-urlencoded",
                        "Encoding": "utf-8",
                        "Connection": "keep-alive",
                        "Accept": "*/*",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "X-Requested-With": "XMLHttpRequest",
                        "Referer": "http://wenshu.court.gov.cn/list/list/?sorttype=1",
                        "Origin": "http://wenshu.court.gov.cn",
                        "Host": "wenshu.court.gov.cn"
                        }
            # yield scrapy.Request(url, body=encodedata,callback=self.parse)
            yield scrapy.FormRequest(url, method='POST',formdata=formdata, callback=self.parse,headers=headers)

    def parse(self, response):
        logging.info("------------parsing--------------"+response.body)
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
