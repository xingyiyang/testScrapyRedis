# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from testredis.items import TestredisItem


class ReadUrlSpider(RedisSpider):
    name = 'read_urls'
    redis_key = 'read_urls:start_urls'

    def parse(self, response):
        zhaoping_list = response.xpath("//table[@class='tablelist']//tr")[1:11]

        for i_item in zhaoping_list:
            zhaoping_item = TestredisItem()
            # 职位名称
            zhaoping_item['zwmc'] = i_item.xpath(".//td[1]//text()").extract_first()
            # 职位类别
            zhaoping_item['zwlb'] = i_item.xpath(".//td[2]//text()").extract_first()
            # 人数
            zhaoping_item['rs'] = i_item.xpath(".//td[3]//text()").extract_first()
            # 地点
            zhaoping_item['dd'] = i_item.xpath(".//td[4]//text()").extract_first()
            # 发布时间
            zhaoping_item['fbsj'] = i_item.xpath(".//td[5]//text()").extract_first()
            print(zhaoping_item)
            # 将数据yield到pipeline里面，进行数据的清洗和存储
            yield zhaoping_item
