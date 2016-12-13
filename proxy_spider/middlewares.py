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

class DebugWenshuSpiderMiddleware(object):
    def process_spider_input(self,response, spider):
        response.replace(body= '''
                        [{\"Count\":\"6209\"},{\"裁判要旨段原文\":\"本院认为：上诉人刘君以非法占有为目的，以虚构事实的手段骗取被害人钱财，其行为已构成诈骗罪，且数额特别巨大，依法应予惩处。鉴于刘君归案后如实供述主要犯罪事实，依法可从轻处罚。一审法院根据刘君犯罪的事实、犯罪的性质、情节和对于社会的危害程度所作判决，事实清楚，证据确实、充分，定性准确，量刑适当，审判程序合法，应予维持。据此，依照《中华人民共和国刑事诉讼法》第二百二十五条第一款第（一）项的规定，裁定如下\",\"案件类型\":\"1\",\"裁判日期\":\"2016-02-25\",\"案件名称\":\"刘君诈骗罪二审刑事裁定书\",\"文书ID\":\"3e9fe83d-8fcc-4d01-aff9-c6512db641be\",\"审判程序\":\"二审\",\"案号\":\"（2016）京刑终18号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，罪犯王金路在死刑缓期二年执行期间，没有故意犯罪，符合法定减刑条件，应予减刑。依照《中华人民共和国刑事诉讼法》第二百五十条第二款及《中华人民共和国刑法》第五十条第一款、第五十七条第一款的规定，裁定如下\",\"案件类型\":\"1\",\"裁判日期\":\"2016-04-12\",\"案件名称\":\"王金路故意杀人罪死缓改无期刑事裁定书\",\"文书ID\":\"449911d8-0096-422c-b278-af4bb60f4491\",\"审判程序\":\"二审\",\"案号\":\"（2016）京刑更9号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，由于原审被告人陈昌明、刘小双、王正辉的故意伤害行为给附带民事诉讼上诉人造成的经济损失，依法应予合理赔偿，并承担连带赔偿责任。附带民事诉讼上诉人及诉讼代理人所提要求赔偿死亡赔偿金、被扶养人生活费的诉讼请求，不属于刑事附带民事诉讼的受案范围，本院不予支持。在本院审理期间，附带民事诉讼上诉人及诉讼代理人没有提交新的依法应予赔偿经济损失的证据，故附带民事诉讼上诉人及诉讼代理人所提要求增加赔偿数额的诉讼请求，理由不足，本院不予支持。原审人民法院根据原审被告人陈昌明、刘小双、王正辉的故意伤害行为给附带民事诉讼上诉人造成经济损失的事实及证据所作的附带民事部分判决，适用法律正确，审判程序合法，应予维持。据此，本院依照《中华人民共和国刑事诉讼法》第二百二十五条第一款第（一）项的规定，裁定如下\",\"案件类型\":\"1\",\"裁判日期\":\"2016-02-05\",\"案件名称\":\"陈昌明等故意伤害罪二审刑事附带民事裁定书\",\"文书ID\":\"0a24acea-5932-4a45-b74d-0f9cce964cb5\",\"审判程序\":\"二审\",\"案号\":\"（2015）高刑终字第604号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，上诉人彭玉江以非法占有为目的，在签订、履行合同过程中，骗取对方当事人钱款，数额巨大，其行为已构成合同诈骗罪，依法应予惩处。&#xA;对于上诉人彭玉江及其辩护人所作的无罪辩解及辩护意见，法庭经审查认为，同案犯韩晓东、王敏、白文龙的供述、证人孔×、孙×等碧水庄园销售人员的证言，以及被害人张×的陈述、彭玉江的供述等在案证据相互印证，能够证明彭玉江作为碧水庄园项目的主要负责人员，明知韩晓东与北年丰村签订的土地承包合同有效期为19年，仍要求销售人员在向被害人张×推销大棚时，虚假承诺使用期限为30年，以及可以在土地上加盖房屋，致使张×陷入错误认识，与忠发天顺公司签订了土地合同，并支付人民币15万元。彭玉江的行为符合合同诈骗罪的构成要件，且认定本案事实的证据均由侦查机关经法定程序依法调取，一审法院采信证据具备客观性、合法性，故对上诉人的辩解、上诉理由及辩护人的辩护意见，本院均不予采纳。&#xA;综上，一审法院根据上诉人彭玉江犯罪的事实，犯罪的性质、情节及对于社会的危害程度所作出的判决，事实清楚，证据确实、充分，定罪及适用法律正确，量刑适当，审判程序合法，应予维持。据此，本院依照《中华人民共和国刑事诉讼法》第二百二十五条第一款第（一）项之规定，裁定如下\",\"案件类型\":\"1\",\"裁判日期\":\"2016-03-14\",\"案件名称\":\"彭玉江合同诈骗罪二审刑事裁定书\",\"文书ID\":\"84d68646-49d2-4544-a0c1-331f98b84cd0\",\"审判程序\":\"二审\",\"案号\":\"（2016）京刑终34号\",\"法院名称\":\"北京市高级人民法院\"},{\"裁判要旨段原文\":\"本院认为，上诉人宋万新以非法占有为目的，在签订、履行合同过程中，骗取对方当事人财物，其行为已构成合同诈骗罪，且数额特别巨大，情节特别严重，依法应予惩处。一审法院根据宋万新犯罪的事实、犯罪的性质、情节和对于社会的危害程度所作判决，事实清楚，证据确实、充分，定性准确，量刑适当，审判程序合法，应予维持。据此，依照《中华人民共和国刑事诉讼法》第二百二十五条第一款第（一）项的规定，裁定如下\",\"案件类型\":\"1\",\"裁判日期\":\"2016-04-18\",\"案件名称\":\"宋万新合同诈骗罪二审刑事裁定书\",\"文书ID\":\"af48cb79-e550-43ca-84c0-c1baa88d78d5\",\"审判程序\":\"二审\",\"案号\":\"（2016）京刑终55号\",\"法院名称\":\"北京市高级人民法院\"}]
                        ''')


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
    def __init__(self):
        self.proxylist = list()
        for item in ProxyItemsTmpDB.get_proxy_items():  
            self.proxylist.append(item)
        print self.proxylist

    def process_request(self, request, spider):
        if not Redis.get(REDIS_PROXY):
            for item in ProxyItemsTmpDB.get_proxy_items():  
                self.proxylist.append(item)
            if self.proxylist:
                if random.random() < 0.5:
                    proxy = self.proxylist[0]
                else:
                    proxy = random.choice(self.proxylist)
                proxy.pop("_id", None)
                Redis.psetex(REDIS_PROXY,1000*3600,json.dumps(proxy))

        proxy = Redis.get(REDIS_PROXY)
        if proxy:
            proxy = json.loads(proxy)
            http_proxy = "http://%s:%s" % (proxy["ip"], proxy["port"])
            request.meta['proxy'] = http_proxy
            print http_proxy
        # else:
        #     #没有代理暂时啥也不做，可以发邮件
        #     raise IgnoreRequest()
    
    def process_exception(self, request, exception, spider):
        proxy = Redis.get(REDIS_PROXY)
        if proxy:
            proxy = json.loads(proxy)
            life = Redis.hget(spider.name,proxy['ip']+':'+proxy['port'])
            if not life:
                Redis.hset(spider.name,proxy['ip']+':'+proxy['port'],2)
            else:
                if int(life)>0:
                    Redis.hset(spider.name,proxy['ip']+':'+proxy['port'],int(life)-1)
                else:
                    print 'dropping ',proxy
                    Redis.psetex(REDIS_PROXY,1,'')
        
        # mailer = MailSender()
        # mailer.send(to=["bangtech@sina.com"], subject="Some subject", body="Some body", cc=["bangtech@sina.com"])
    



