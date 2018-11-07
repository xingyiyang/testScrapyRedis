# -*- coding: utf-8 -*-
import scrapy
import redis

r = redis.Redis(host='localhost', port=6379)
r.lpush('read_urls:start_urls', 'https://hr.tencent.com/position.php')
class GeturlsSpider(scrapy.Spider):
    name = 'get_job'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        # 解析下一页
        next_link = response.xpath("//div[@class='pagenav']//a[@id='next']//@href").extract()
        new_url = "https://hr.tencent.com/"+next_link[0]

        if next_link:
            r.lpush('read_urls:start_urls', new_url)
            yield scrapy.Request(new_url, callback=self.parse)
