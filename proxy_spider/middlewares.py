# -*- coding:utf-8 -*-
__author__ = 'Mr.Tian'

import base64
import random
from proxy_spider.db.mongo import ProxyItemsTmpDB
import logging
from db.mredis import Redis
from settings import REDIS_PROXY
from scrapy.mail import MailSender
import json
import scrapy_proxies

class RandomUserAgentMiddleware(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ProxyMiddleware(object):
    # def __init__(self):
    #     self.proxylist = list()
    #     for item in ProxyItemsTmpDB.get_proxy_items():  
    #         self.proxylist.append(item)
    #     print self.proxylist

    def process_request(self, request, spider):
        print request
        pass

        # if not Redis.get(REDIS_PROXY):
        #     for item in ProxyItemsTmpDB.get_proxy_items():  
        #         self.proxylist.append(item)
        #     if self.proxylist:
        #         if random.random() < 0.5:
        #             proxy = self.proxylist[0]
        #         else:
        #             proxy = random.choice(self.proxylist)
        #         proxy.pop("_id", None)
        #         Redis.psetex(REDIS_PROXY,1000*3600,json.dumps(proxy))

        # proxy = Redis.get(REDIS_PROXY)
        # if proxy:
        #     proxy = json.loads(proxy)
        #     http_proxy = "http://%s:%s" % (proxy["ip"], proxy["port"])
        #     request.meta['proxy'] = http_proxy
        #     print http_proxy
    
    # def process_exception(self, request, exception, spider):
    #     proxy = Redis.get(REDIS_PROXY)
    #     if proxy:
    #         proxy = json.loads(proxy)
    #         life = Redis.hget(spider.name,proxy['ip']+':'+proxy['port'])
    #         if not life:
    #             Redis.hset(spider.name,proxy['ip']+':'+proxy['port'],2)
    #         else:
    #             if int(life)>0:
    #                 Redis.hset(spider.name,proxy['ip']+':'+proxy['port'],int(life)-1)
    #             else:
    #                 print 'dropping ',proxy
    #                 Redis.psetex(REDIS_PROXY,1,'')
        
   



