# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from acm_scraper.tools import rightmove


class RightmoveSpider(scrapy.Spider):
    name = "rightmove"
    allowed_domains = ["rightmove.co.uk"]
    start_urls = ['http://www.rightmove.co.uk/overseas-property-for-sale/\
Bulgaria.html?sortType=2&currencyCode=USD']

    def parse(self, response):
        items_xp = "//li[@name='summary-list-item']/.//a[@class='photo']/@href"
        for url in response.xpath(items_xp).extract():
            url = response.urljoin(url)
            yield Request(url, callback=self.parse_item)

        next_xp = "//a[contains(text(), 'next')]/@href"
        next_url = response.xpath(next_xp).extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield Request(next_url, callback=self.parse)

    def parse_item(self, response):
        item = dict()
        item_parser = rightmove.RmItemParser(response)

        item['url'] = response.url
        item['name'] = item_parser.name
        item['price'] = item_parser.price
        item['bedrooms'] = item_parser.bedrooms
        item['Location'] = item_parser.location
        item['features'] = item_parser.features

        yield item
