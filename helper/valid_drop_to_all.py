# -*- coding:utf-8 -*-
__author__ = 'Mr.Tian'


from log import init_logging
from mongo import ProxyItemsDB, ProxyItemsDropDB, ProxyItemsDropForeverDB

from valid_proxy import valid_proxy
from get_proxy import GetProxy



def main():
    get_proxy = GetProxy(ProxyItemsDropDB)
    while True:
        item = get_proxy.get_proxy()
        ret = valid_proxy(item)
        if ret:
            ProxyItemsDB.upsert_proxy_item(ret)
            ProxyItemsDropDB.remove_proxy_item(item)
            pass
        else:
            ProxyItemsDropDB.remove_proxy_item(item)
            ProxyItemsDropForeverDB.upsert_proxy_item(item)


if __name__ == "__main__":
    init_logging("log/valid_drop_to_all.log", "log/valid_drop_to_all_2.log")
    main()
    pass
