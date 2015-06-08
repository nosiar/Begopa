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
    start_urls = ['http://blog.naver.com/PostListByTagName.nhn?blogId=begopa1092&logType=0&cpage=18&tagName=%BF%D5%C1%C1%BE%C6']

    def parse(self, response):
        sel = Selector(response)
        post_list = sel.xpath('//div[@id="tag_list"]/table/tr/td/div/div[@class="list"]')

        print(len(post_list))
        for post in post_list:
            location = post.xpath('p[@class="tit"]/a/text()')[0].extract().split('/')
            
            item = WangjoaItem()
            item['url'] = post.xpath('p[@class="tit"]/a/@href')[0].extract();
            item['name'] = location[1].strip()
            item['location'] = post.xpath('p[@class="tit"]/span/text()')[0].extract();
            item['location_detail'] = location[0].strip()
            item['excerpt'] = post.xpath('p[@class="con"]/a/text()')[0].extract();

            yield item

