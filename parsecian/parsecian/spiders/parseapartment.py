import scrapy


class ParseapartmentSpider(scrapy.Spider):
    name = "parseapartment"
    allowed_domains = ["kazan.cian.ru"]

    start_urls = [
        "https://kazan.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=4777&room1=1"]

    def parse(self, response):
        apartments = response.xpath('//div')


        for apartment in apartments:

            yield {
                'a':1
                # 'title': apartment.xpath(
                #     './/div[@class="_93444fe79c--container--aWzpE"]/span/text()').get()
            }
                # 'count_room': apartment.xpath('.//div[@class="_93444fe79c--row--kEHOK"]/a/span/span').get().split()
        pass

