# -*- coding:utf-8 -*-
__author__ = 'Mr.Tian'


from log import init_logging
from mongo import ProxyItemsDB, ProxyItemsDropDB, ProxyItemsTmpDB

from valid_proxy import valid_proxy
from get_proxy import GetProxy



def main():
    get_proxy = GetProxy(ProxyItemsTmpDB)
    while True:
        item = get_proxy.get_proxy()
        ret = valid_proxy(item)
        if ret:
            ProxyItemsDB.upsert_proxy_item(ret)
            pass
        else:
            ProxyItemsDropDB.upsert_proxy_item(item)
            pass
        ProxyItemsTmpDB.remove_proxy_item(item)

    pass


if __name__ == "__main__":
    init_logging("log/valid_tmp.log", "log/valid_tmp_2.log")
    main()
    pass
