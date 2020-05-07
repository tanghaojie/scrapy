# -*- coding: utf-8 -*-
import scrapy
from jt.items import eyouItem

class EyouSpider(scrapy.Spider):
    name = 'eyou'
    allowed_domains = ['http://scchzz.ch.mnr.gov.cn']
    start_urls = ['http://scchzz.ch.mnr.gov.cn/']

    nowPage = 2
    maxPage = 21

    def start_requests(self):
        url = 'http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516'
        data =  {
            'ScriptManager1': 'ScriptManager1|BtnSearch',
            'DropLevl': '2',
            'txtYear': '2019',
            'PageTurnControl1$SelectPageSize': '15',
            'PageTurnControl1$ANPager_input': '2',
            'PageTurnControl1$HiddenPageSize': '15',
            'PageTurnControl2$SelectPageSize': '10',
            '__VIEWSTATE': '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'
        }
        yield scrapy.FormRequest(url, method = 'POST', formdata=data, callback = self.parse, dont_filter = True)

    def parse(self, response):
        viewstate = response.xpath('//form/input[@id="__VIEWSTATE"]/@value').extract_first()

        x = response.xpath('''//form/div[@id="rotate"]
        /div/table/tr[@id="fragment-1"]/td/div[@id="UpdatePanel5"]
        /table[1]/tr''')
        print('---------------------------')

        for i in range(len(x)):
        # for i in range(2):
            if i==0:
                continue
            item = eyouItem()
            row = x[i].xpath('td')
            item['order'] = row[0].xpath('text()').extract_first().strip()
            item['loc'] = row[1].xpath('text()').extract_first().strip()
            item['name'] = row[2].xpath('a/text()').extract_first().strip()
            item['level'] = row[3].xpath('text()').extract_first().strip()
            item['legal'] = row[4].xpath('text()').extract_first().strip()

            id_level = row[2].xpath('a/@onclick').extract_first()
            id_level = id_level[9:len(id_level)-1]
            id_level = id_level.split(',')
            idstr = id_level[0]
            levelstr = id_level[1]

            yield scrapy.Request('http://scchzz.ch.mnr.gov.cn/PorttalWeb/UnitBaseInfoView.aspx?ID=%s&Level=%s' % (idstr, levelstr),
                             callback=self.detail_parse, meta={'item': item}, dont_filter=True)

        while(self.nowPage <= self.maxPage):
            url = 'http://scchzz.ch.mnr.gov.cn/Index/QueryList.aspx?AreaId=2516'
            data =  {
                'ScriptManager1': 'UpdatePanel5|PageTurnControl1$ANPager',
                'DropLevl': '2',
                'txtYear': '2019',
                'PageTurnControl1$SelectPageSize': '15',
                'PageTurnControl1$ANPager_input': str(self.nowPage - 1),
                'PageTurnControl1$HiddenPageSize': '15',
                'PageTurnControl2$SelectPageSize': '10',
                '__EVENTTARGET': 'PageTurnControl1$ANPager',
                '__EVENTARGUMENT': str(self.nowPage),
                '__VIEWSTATE': viewstate
            }
            self.nowPage += 1
            yield scrapy.FormRequest(url, method = 'POST', formdata=data, callback = self.parse, dont_filter = True)

    def detail_parse(self, response):
        item = response.meta['item']
        table = response.xpath('''//form/table[@class="tbl"]/tr''')

        item['locdetail'] = table[2].xpath('td[2]/span[@id="lblOfficeAddress"]/text()').extract_first().strip()
        item['contact'] = table[3].xpath('td[4]/span[@id="lblContact"]/text()').extract_first().strip()
        item['phone'] = table[4].xpath('td[2]/span[@id="lblTelNumber"]/text()').extract_first().strip()
        item['certiCode'] = table[4].xpath('td[4]/span[@id="lblCertificateCode"]/text()').extract_first().strip()
        item['issueDate'] = table[5].xpath('td[2]/span[@id="lblIssueDate"]/text()').extract_first().strip()
        item['effectiveDate'] = table[5].xpath('td[4]/span[@id="lblEffectiveDate"]/text()').extract_first().strip()
        item['businessScope'] = table[6].xpath('td[2]/span[@id="lblBusinessScopeList"]/text()').extract_first().strip()

        return item
