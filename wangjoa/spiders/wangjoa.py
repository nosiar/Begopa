# -*- coding: utf-8 -*-

from __future__ import absolute_import
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from wangjoa.items import WangjoaItem

class WangjoaSpider(Spider):

    name = 'wangjoa'
    allowed_domains = ['naver.com']
    url_format = 'http://blog.naver.com/PostListByTagName.nhn?blogId=begopa1092&logType=0&cpage={0}&tagName=%BF%D5%C1%C1%BE%C6'
    start_urls = [url_format.format(1)]

    def parse(self, response):
        sel = Selector(response)

        page_list = sel.xpath('//table[@class="page-navigation"]/tr/td/a/text()').extract()
        for page in page_list:
            yield Request(self.url_format.format(page), callback=self.parse_page)
      
        has_next_page = sel.xpath('//table[@class="page-navigation"]/tr/td/a/span[@class="arw"]/text()')[0].extract() == u'▶'
        if(has_next_page):
            yield Request(self.url_format.format(int(page_list[-1]) + 1), callback=self.parse, dont_filter=True)

    def parse_page(self, response):
        sel = Selector(response)

        post_list = sel.xpath('//div[@id="tag_list"]/table/tr/td/div/div[@class="list"]')

        for post in post_list:
            location = post.xpath('p[@class="tit"]/a/text()')[0].extract().split('/')
            if len(location) < 2:
                continue
            
            item = WangjoaItem()
            item['url'] = post.xpath('p[@class="tit"]/a/@href')[0].extract();
            item['name'] = location[1].strip()
            item['location'] = post.xpath('p[@class="tit"]/span/text()')[0].extract();
            item['location_detail'] = location[0].strip()
            item['excerpt'] = post.xpath('p[@class="con"]/a/text()')[0].extract();

            yield item

