# -*- coding:utf-8 -*-
__author__ = 'Mr.Tian'

import scrapy

from ..items import ProxyItem


class ProxyIpSpider(scrapy.Spider):
    name = "proxy_ip_spider"
    allowed_domains = [
        "proxy-ip.cn"
    ]

    # start_urls = [
    #     "http://ip84.com/dl"
    # ]

    custom_settings = {
        'LOG_FILE': 'log/proxy_ip.log'
    }

    def start_requests(self):
        for i in ['guonei']:
            for j in range(1, 40):  # page
                url = "http://www.proxy-ip.cn/%s/%s" % (i, j)
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # print "parse"

        for trs in response.xpath('//tr'):
            tds = trs.xpath('.//td')
            if len(tds) < 7:
                continue
            proxy_item = ProxyItem()
            # proxy_item['country'] = tds[0].xpath('.//img/@alt').extract_first()
            proxy_item['ip'] = tds[0].xpath('.//text()').extract_first().strip()
            proxy_item['port'] = tds[1].xpath('.//text()').extract_first().strip()
            proxy_item['location'] = tds[2].xpath('.//text()').extract_first()
            proxy_item['type'] = tds[3].xpath('.//text()').extract_first().strip()
            proxy_item['anonymous'] = tds[4].xpath('.//text()').extract_first().strip()
            proxy_item['time'] = tds[5].xpath('.//text()').extract_first().strip()
            proxy_item['speed'] = tds[6].xpath('.//text()').extract_first().strip()

            yield proxy_item