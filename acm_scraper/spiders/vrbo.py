# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from acm_scraper.tools import vrbo


class VrboSpider(scrapy.Spider):
    name = "vrbo"
    allowed_domains = ["vrbo.com"]
    start_urls = ['http://www.vrbo.com/vacation-rentals/\
europe/hungary/budapest/']

    def parse(self, response):
        items_xp = "//ul[@id='property-list-group']/li/@data-listingurl"
        for url in response.xpath(items_xp).extract():
            url = response.urljoin(url)
            yield Request(url, callback=self.parse_item)

        next_xp = "//link[@rel='next']/@href"
        next_url = response.xpath(next_xp).extract_first()
        if next_url:
            yield Request(next_url, callback=self.parse)

    def parse_item(self, response):
        # • Name
        # • Rate
        # • Bedrooms
        # • Bathrooms
        # • Sleeps
        # • location
        # • Rating
        # • Rating count
        # • View count
        item = dict()
        item_parser = vrbo.VrboParser(response)

        item['url'] = item_parser.url
        item['name'] = item_parser.name
        item['rating'] = item_parser.rating
        item['rating_count'] = item_parser.rating_count
        item['bedrooms'] = item_parser.bedrooms
        item['bathrooms'] = item_parser.bathrooms
        item['sleeps'] = item_parser.sleeps
        item['location'] = item_parser.location
        item['rate'] = item_parser.rate

        yield item
