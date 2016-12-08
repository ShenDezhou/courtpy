# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from proxy_spider.db.mongo import ProxyItemsTmpDB

from db.mredis import Redis
import dateutil.parser


class ValidParamsPipeline(object):
    def process_item(self, item, spider):
        if spider.name=="wenshu_spider":
            return item
        
        try:
            if item["ip"] and item["port"] and (0 < int(item['port']) < 65535):
                return item
            raise DropItem("params not Valid: %s:%s" % (item.get("ip"), item.get("port")))
        except Exception, e:
            raise DropItem("params not Valid: %s:%s" % (item.get("ip"), item.get("port")))


class DuplicatesPipeline(object):
    def __init__(self):
        self.ips_seen = set()

    def process_item(self, item, spider):
        if spider.name=="wenshu_spider":
            return item
        
        ip_port = '%s:%s' % (item['ip'], item['port'])
        if ip_port in self.ips_seen:
            raise DropItem("Duplicate item found: %s" % ip_port)
        else:
            self.ips_seen.add(ip_port)
            return item


class TimeProcessPipeline(object):
    def process_item(self, item, spider):
        if spider.name=="wenshu_spider":
            return item
        
        if item.get('time'):
            item['time'] = dateutil.parser.parse(item['time']).strftime('%Y-%m-%d %H:%M:%S')
        return item


class RedisPipeline(object):
    def process_item(self, item, spider):
        if spider.name=="wenshu_spider":
            return item
        
        Redis.r.hset(spider.name,item['ip']+':'+item['port'],item)
        return item	

class MongoPipeline(object):
    def process_item(self, item, spider):
        if spider.name=="wenshu_spider":
            WenshuItemsDB.upsert_proxy_item(dict(item))
            return item
        
        ProxyItemsTmpDB.upsert_proxy_item(dict(item))
        return item
