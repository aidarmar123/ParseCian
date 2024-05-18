import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ParsingspiderSpider(CrawlSpider):
    name = "parsingSpider"
    allowed_domains = ["kazan.cian.ru"]
    start_urls = ["https://kazan.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=4777&room1=1"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="_93444fe79c--media--9P6wN"]'), callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="_93444fe79c--pages-list--gsEUE"]/../a'),  callback='parse_links', follow=True)
            )
    
    link_counter=1
    def parse_item(self, response):
        item = {}
        
        item["title"] = response.xpath('//h1[@class="a10a3f92e9--title--vlZwT"]/text()').get()
        item["count_room"]=response.xpath('//h1[@class="a10a3f92e9--title--vlZwT"]/text()').get().split()[1]
        item["square"]=response.xpath('//span[text()="Общая площадь"]/../span[contains(text(),"м²")]/text()').get()
        item["floor"]=response.xpath('//span[text()="Этаж"]/../span[contains(text(),"из")]/text()').get()
        for part_adress in response.xpath('//div[@data-name="AddressContainer"]'):
            item["street"]=part_adress.xpath('.//a/text()').getall()
        item["price"]=response.xpath('//span[contains(text(),"₽") and @class="a10a3f92e9--color_black_100--Ephi7 a10a3f92e9--lineHeight_9u--limEs a10a3f92e9--fontWeight_bold--BbhnX a10a3f92e9--fontSize_28px--P1gR4 a10a3f92e9--display_block--KYb25 a10a3f92e9--text--e4SBY" ]/text()').get()
        item["id"] = response.url.split('/')[-2]
        item["page_number"]=self.link_counter
        return item
    def parse_links(self, response):
        self.link_counter += 1