import re


class RmItemParser:
    def __init__(self, response):
        self.xpath = response.xpath
        # with open("out.html", "w") as out:
        #     out.write(response.text)

    @property
    def name(self):
        name_xp = "//*[@id='propertytype']/text()"
        try:
            name = self.xpath(name_xp).extract()[0]
            return name.strip()
        except IndexError:
            return None

    @property
    def price(self):
        price_xp = "//span[@class='mainPriceSubText']/text()"
        try:
            price = self.xpath(price_xp).extract()[0]
            return price.strip("()")
        except IndexError:
            return None

    @property
    def bedrooms(self):
        name = self.name
        res = re.search("\d+ bedroom", name)
        if res:
            name = res.group()
            res = re.search("\d+", name)
            if res:
                return res.group()

        return None

    @property
    def location(self):
        loc_xp = "//*[@id='addresscontainer']/h2/text()"
        try:
            loc = self.xpath(loc_xp).extract()[0]
            return loc.strip()
        except IndexError:
            return None

    @property
    def features(self):
        feat_xp = "//ul[@class='keyfeatures']/li/text()"
        feat_list = self.xpath(feat_xp).extract()
        return feat_list
