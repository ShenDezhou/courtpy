# -*- coding:utf-8 -*-
__author__ = 'Mr.Tian'


from log import init_logging
from mongo import ProxyItemsDB, ProxyItemsDropDB

from valid_proxy import valid_proxy



def main():
    cur = ProxyItemsDB.get_proxy_items()
    for item in cur:
        ret = valid_proxy(item)
        if ret:
            ProxyItemsDB.remove_proxy_item(item)
            ProxyItemsDB.upsert_proxy_item(ret)
            pass
        else:
            ProxyItemsDB.remove_proxy_item(item)
            ProxyItemsDropDB.upsert_proxy_item(item)
            pass
    pass


if __name__ == "__main__":
    init_logging("log/valid_all_to_drop.log", "log/valid_all_to_drop_2.log")
    main()
    pass
