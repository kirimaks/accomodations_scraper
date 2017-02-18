import re


class VrboParser:
    def __init__(self, response):
        self.xpath = response.xpath
        self.response = response

    @property
    def url(self):
        return self.response.url

    @property
    def name(self):
        name_xp = "//*[@itemprop='name']/@content"
        try:
            name = self.xpath(name_xp).extract()[0]
            return name.strip()

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
    def bedrooms(self):
        bedrooms_xp = "//b[contains(text(), 'Bedrooms:')]/\
following-sibling::span/text()"
        try:
            bedrooms = self.xpath(bedrooms_xp).extract()[0]
            return bedrooms.strip()
        except IndexError:
            return None

    @property
    def bathrooms(self):
        bathrooms_xp = "//b[contains(text(), 'Bathrooms:')]/\
following-sibling::span/text()"
        try:
            bathrooms = self.xpath(bathrooms_xp).extract()[0]
            return bathrooms.strip()
        except IndexError:
            return None

    @property
    def sleeps(self):
        sleeps_xp = "//b[contains(text(), 'Sleeps:')]/\
following-sibling::span/text()"
        try:
            sleeps = self.xpath(sleeps_xp).extract()[0]
            return sleeps.strip()
        except IndexError:
            return None

    @property
    def location(self):
        location_xp = "//meta[@name='Location']/@content"
        try:
            location = self.xpath(location_xp).extract()[0]
            location = re.sub(">", ",", location)
            return location.strip()

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

    @property
    def rate(self):
        rate_xp = "//body/@data-averagenightly"
        try:
            rate = self.xpath(rate_xp).extract()[0]
            return rate.strip()
        except IndexError:
            return None
