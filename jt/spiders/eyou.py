# -*- coding: utf-8 -*-
import scrapy
from jt.items import eyouItem
from urllib.parse import urlparse
'''
四川 http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516
北京 http://bjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2
天津 http://tjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=21
内蒙 http://nmchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=383
山西 http://sxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=241
河北 http://hebchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=28
湖北 http://hbchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1866
湖南 http://hnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1996
江西 http://jxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1373
河南 http://henchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1671
上海 http://shchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=867
山东 http://sdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1496
江苏 http://jschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=887
浙江 http://zjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1018
安徽 http://ahchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1131
福建 http://fjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1269
广东 http://gdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2146
广西 http://gxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2308
海南 http://hichzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2446
辽宁 http://lnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=506
吉林 http://jlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=635
黑龙江 http://hlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=713
陕西 http://snchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3076
甘肃 http://gschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3204
青海 http://qhchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3317
宁夏 http://nxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3370
新疆 http://xjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3403
重庆 http://cqchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2475
贵州 http://gzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2737
云南 http://ynchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2840
西藏 http://xzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2994
'''
'''
http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516
http://bjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2
http://tjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=21
http://nmchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=383
http://sxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=241
http://hebchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=28
http://hbchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1866
http://hnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1996
http://jxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1373
http://henchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1671
http://shchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=867
http://sdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1496
http://jschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=887
http://zjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1018
http://ahchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1131
http://fjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1269
http://gdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2146
http://gxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2308
http://hichzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2446
http://lnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=506
http://jlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=635
http://hlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=713
http://snchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3076
http://gschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3204
http://qhchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3317
http://nxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3370
http://xjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3403
http://cqchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2475
http://gzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2737
http://ynchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2840
http://xzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2994
'''


class EyouSpider(scrapy.Spider):
    name = 'eyou'
    # allowed_domains = ['scchzz.ch.mnr.gov.cn', 'xzchzz.ch.mnr.gov.cn']
    # start_urls = ['http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516', 'http://xzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2994']
    # now = {
    #     'http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516': 2,
    #     'http://xzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2994': 2
    # }
    allowed_domains = [
        'scchzz.ch.mnr.gov.cn'
        'bjchzz.ch.mnr.gov.cn'
        'tjchzz.ch.mnr.gov.cn'
        'nmchzz.ch.mnr.gov.cn'
        'sxchzz.ch.mnr.gov.cn'
        'hebchzz.ch.mnr.gov.cn'
        'hbchzz.ch.mnr.gov.cn'
        'hnchzz.ch.mnr.gov.cn'
        'jxchzz.ch.mnr.gov.cn'
        'henchzz.ch.mnr.gov.cn'
        'shchzz.ch.mnr.gov.cn'
        'sdchzz.ch.mnr.gov.cn'
        'jschzz.ch.mnr.gov.cn'
        'zjchzz.ch.mnr.gov.cn'
        'ahchzz.ch.mnr.gov.cn'
        'fjchzz.ch.mnr.gov.cn'
        'gdchzz.ch.mnr.gov.cn'
        'gxchzz.ch.mnr.gov.cn'
        'hichzz.ch.mnr.gov.cn'
        'lnchzz.ch.mnr.gov.cn'
        'jlchzz.ch.mnr.gov.cn'
        'hlchzz.ch.mnr.gov.cn'
        'snchzz.ch.mnr.gov.cn'
        'gschzz.ch.mnr.gov.cn'
        'qhchzz.ch.mnr.gov.cn'
        'nxchzz.ch.mnr.gov.cn'
        'xjchzz.ch.mnr.gov.cn'
        'cqchzz.ch.mnr.gov.cn'
        'gzchzz.ch.mnr.gov.cn'
        'ynchzz.ch.mnr.gov.cn'
        'xzchzz.ch.mnr.gov.cn'
    ]
    start_urls = [
        'http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516',
        'http://bjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2',
        'http://tjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=21',
        'http://nmchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=383',
        'http://sxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=241',
        'http://hebchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=28',
        'http://hbchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1866',
        'http://hnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1996',
        'http://jxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1373',
        'http://henchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1671',
        'http://shchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=867',
        'http://sdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1496',
        'http://jschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=887',
        'http://zjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1018',
        'http://ahchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1131',
        'http://fjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1269',
        'http://gdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2146',
        'http://gxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2308',
        'http://hichzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2446',
        'http://lnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=506',
        'http://jlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=635',
        'http://hlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=713',
        'http://snchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3076',
        'http://gschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3204',
        'http://qhchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3317',
        'http://nxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3370',
        'http://xjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3403',
        'http://cqchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2475',
        'http://gzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2737',
        'http://ynchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2840',
        'http://xzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2994'
    ]
    now = {
        'http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516': 2,
        'http://bjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2': 2,
        'http://tjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=21': 2,
        'http://nmchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=383': 2,
        'http://sxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=241': 2,
        'http://hebchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=28': 2,
        'http://hbchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1866': 2,
        'http://hnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1996': 2,
        'http://jxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1373': 2,
        'http://henchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1671': 2,
        'http://shchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=867': 2,
        'http://sdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1496': 2,
        'http://jschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=887': 2,
        'http://zjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1018': 2,
        'http://ahchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1131': 2,
        'http://fjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1269': 2,
        'http://gdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2146': 2,
        'http://gxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2308': 2,
        'http://hichzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2446': 2,
        'http://lnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=506': 2,
        'http://jlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=635': 2,
        'http://hlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=713': 2,
        'http://snchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3076': 2,
        'http://gschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3204': 2,
        'http://qhchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3317': 2,
        'http://nxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3370': 2,
        'http://xjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3403': 2,
        'http://cqchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2475': 2,
        'http://gzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2737': 2,
        'http://ynchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2840': 2,
        'http://xzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2994': 2
    }
    region = {
        'http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516': '四川',
        'http://bjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2': '北京',
        'http://tjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=21': '天津',
        'http://nmchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=383': '内蒙',
        'http://sxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=241': '山西',
        'http://hebchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=28': '河北',
        'http://hbchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1866': '湖北',
        'http://hnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1996': '湖南',
        'http://jxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1373': '江西',
        'http://henchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1671': '河南',
        'http://shchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=867': '上海',
        'http://sdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1496': '山东',
        'http://jschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=887': '江苏',
        'http://zjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1018': '浙江',
        'http://ahchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1131': '安徽',
        'http://fjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=1269': '福建',
        'http://gdchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2146': '广东',
        'http://gxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2308': '广西',
        'http://hichzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2446': '海南',
        'http://lnchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=506': '辽宁',
        'http://jlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=635': '吉林',
        'http://hlchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=713': '黑龙江',
        'http://snchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3076': '陕西',
        'http://gschzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3204': '甘肃',
        'http://qhchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3317': '青海',
        'http://nxchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3370': '宁夏',
        'http://xjchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=3403': '新疆',
        'http://cqchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2475': '重庆',
        'http://gzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2737': '贵州',
        'http://ynchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2840': '云南',
        'http://xzchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2994': '西藏'
    }
    level = '3'

    def parse(self, response):
        viewstate = response.xpath(
            '//form/input[@id="__VIEWSTATE"]/@value').extract_first()
        data = {
            'ScriptManager1': 'ScriptManager1|BtnSearch',
            'DropLevl': self.level,
            'txtYear': '2019',
            'PageTurnControl1$SelectPageSize': '15',
            'PageTurnControl1$ANPager_input': '2',
            'PageTurnControl1$HiddenPageSize': '15',
            'PageTurnControl2$SelectPageSize': '10',
            '__VIEWSTATE': viewstate
        }
        yield scrapy.FormRequest(response.url,
                                 method='POST',
                                 formdata=data,
                                 callback=self.main_parse,
                                 dont_filter=True)

    def main_parse(self, response):
        viewstate = response.xpath(
            '//form/input[@id="__VIEWSTATE"]/@value').extract_first()

        d = response.xpath('''//form/div[@id="rotate"]
        /div/table/tr[@id="fragment-1"]/td/div[@id="UpdatePanel5"]
        /table[2]/tr/td[@id="PageTurnControl1_ANPager_Holder"]
        /div[@id="PageTurnControl1_ANPager"]/div
        /input[@id="PageTurnControl1$ANPager_btn"]/@onclick''').extract_first(
        )
        d = d.replace("if(ANP_checkInput('PageTurnControl1$ANPager_input',",
                      '')
        d = d.replace(
            ")){__doPostBack('PageTurnControl1$ANPager','')} else{return false}",
            '')
        maxPage = int(d)

        x = response.xpath('''//form/div[@id="rotate"]
        /div/table/tr[@id="fragment-1"]/td/div[@id="UpdatePanel5"]
        /table[1]/tr''')

        for i in range(len(x)):
            if i == 0:
                continue
            item = eyouItem()
            row = x[i].xpath('td')

            item['order'] = row[0].xpath('text()').extract_first().strip()
            item['region'] = self.region[response.url]
            item['loc'] = row[1].xpath('text()').extract_first().strip()
            item['name'] = row[2].xpath('a/text()').extract_first().strip()
            item['level'] = row[3].xpath('text()').extract_first().strip()
            item['legal'] = row[4].xpath('text()').extract_first().strip()

            id_level = row[2].xpath('a/@onclick').extract_first()
            id_level = id_level[9:len(id_level) - 1]
            id_level = id_level.split(',')
            idstr = id_level[0]
            levelstr = id_level[1]

            result = urlparse(response.url)
            domain = result.scheme + '://' + result.netloc
            yield scrapy.Request(
                domain + '/PorttalWeb/UnitBaseInfoView.aspx?ID=%s&Level=%s' %
                (idstr, levelstr),
                callback=self.detail_parse,
                meta={'item': item},
                dont_filter=True)

        while (self.now[response.url] <= maxPage):
            data = {
                'ScriptManager1': 'UpdatePanel5|PageTurnControl1$ANPager',
                'DropLevl': self.level,
                'txtYear': '2019',
                'PageTurnControl1$SelectPageSize': '15',
                'PageTurnControl1$ANPager_input':
                str(self.now[response.url] - 1),
                'PageTurnControl1$HiddenPageSize': '15',
                'PageTurnControl2$SelectPageSize': '10',
                '__EVENTTARGET': 'PageTurnControl1$ANPager',
                '__EVENTARGUMENT': str(self.now[response.url]),
                '__VIEWSTATE': viewstate
            }
            self.now[response.url] += 1
            yield scrapy.FormRequest(response.url,
                                     method='POST',
                                     formdata=data,
                                     callback=self.main_parse,
                                     dont_filter=True)

    def detail_parse(self, response):
        item = response.meta['item']
        table = response.xpath('''//form/table[@class="tbl"]/tr''')

        item['locdetail'] = table[2].xpath(
            'td[2]/span[@id="lblOfficeAddress"]/text()').extract_first().strip(
            )
        item['contact'] = table[3].xpath(
            'td[4]/span[@id="lblContact"]/text()').extract_first().strip()
        item['phone'] = table[4].xpath(
            'td[2]/span[@id="lblTelNumber"]/text()').extract_first().strip()
        item['certiCode'] = table[4].xpath(
            'td[4]/span[@id="lblCertificateCode"]/text()').extract_first(
            ).strip()
        item['issueDate'] = table[5].xpath(
            'td[2]/span[@id="lblIssueDate"]/text()').extract_first().strip()
        item['effectiveDate'] = table[5].xpath(
            'td[4]/span[@id="lblEffectiveDate"]/text()').extract_first().strip(
            )
        item['businessScope'] = table[6].xpath(
            'td[2]/span[@id="lblBusinessScopeList"]/text()').extract_first(
            ).strip()

        return item
