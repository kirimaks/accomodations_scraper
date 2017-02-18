import re


class HomeParser:
    def __init__(self, response):
        self.xpath = response.xpath
        self.response = response

    @property
    def url(self):
        return self.response.url

    @property
    def name(self):
        name_xp = "//h1[@class='listing-headline ']/span/text()"
        try:
            name = self.xpath(name_xp).extract()[0]
            return name.strip()
        except IndexError:
            return None

    @property
    def rate(self):
        rate_xp = "//div[@class='price-large js-fromPriceValue']/text()"
        try:
            rate = self.xpath(rate_xp).extract()[0]
            return rate.strip()
        except IndexError:
            return None

    @property
    def bedrooms(self):
        bedrooms_xp = "//td[contains(text(), 'Bedrooms')]/\
following-sibling::td/text()"
        try:
            bedrooms = self.xpath(bedrooms_xp).extract()[0]
            return bedrooms.strip()
        except IndexError:
            return None

    @property
    def bathrooms(self):
        bathrooms_xp = "//td[contains(text(), 'Bathrooms')]/\
following-sibling::td/text()"
        try:
            bathrooms = self.xpath(bathrooms_xp).extract()[0]
            return bathrooms.strip()
        except IndexError:
            return None

    @property
    def sleeps(self):
        resp = re.search(r'\d+ Sleeps|Sleeps \d+', self.response.text)
        if resp:
            resp = resp.group()
            num = re.search(r'\d+', resp)
            if num:
                return num.group().strip()

        return None

    @property
    def location(self):
        loc_xp = "//a[@class='js-breadcrumbLink']/text()"
        try:
            loc = self.xpath(loc_xp).extract()[0]
            return loc.strip()
        except IndexError:
            return None

    @property
    def rating(self):
        rating_xp = "//meta[@itemprop='ratingValue']/@content"
        try:
            rating = self.xpath(rating_xp).extract()[0]
            return rating.strip()
        except IndexError:
            return None

    @property
    def rating_count(self):
        rt_count_xp = "//meta[@itemprop='reviewCount']/@content"
        try:
            rt_count = self.xpath(rt_count_xp).extract()[0]
            return rt_count.strip()
        except IndexError:
            return None
