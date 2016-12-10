# -*- coding:utf-8 -*-
__author__ = 'Mr.Tian'

import pymongo
import time
# MONGO
MONGO_URI = "localhost:27017"
MONGO_PROXY_DB = "proxy"

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]

def get_mongo_find_dict(hours_ago = 4):
    GOOD_PROXY_CONDITION = { 'time' :{'$gt' :'%s'%time.strftime('%Y-%m-%d %H:00:00', time.localtime(time.time()-hours_ago*3600)),
        '$lt' :'%s'%time.strftime('%Y-%m-%d %H:59:59', time.localtime(time.time()))}, 'type':'HTTP'}, {'_id': 0}  
    return GOOD_PROXY_CONDITION

class ProxyItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_all.find({}, {'_id': 0}).batch_size(50)

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_all.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_all.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsDropDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_drop.find({}, {'_id': 0}).batch_size(50)

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_drop.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_drop.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsTmpDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        hour_interval = [1,2,4,8,12,24,36,48,65535]
        for i in hour_interval:
            if proxy_db.proxy_items_tmp.count(get_mongo_find_dict(i)):
                return proxy_db.proxy_items_tmp.find(get_mongo_find_dict()).batch_size(50)
        return proxy_db.proxy_items_tmp.find({}, {'_id': 0}).batch_size(50)
        
    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_tmp.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_tmp.remove({"ip": item['ip'], "port": item['port']})

class WenshuItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_all.find({}, {'_id': 0}).batch_size(50)

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_all.update({"id": item['id']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_all.remove({"id": item['id']})

