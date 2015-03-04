from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from wangjoa.items import WangjoaItem

class WangjoaSpider(Spider):
    
    name = 'wangjoa'
    allowed_domain = ['naver.com']
    start_url = ['http://blog.naver.com/PostListByTagName.nhn?blogId=begopa1092&logType=mylog&tagName=%BF%D5%C1%C1%BE%C6']

    def parse(self, response):
        pass


