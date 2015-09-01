import scrapy
from school.items import SchoolItem

class StateSpider(scrapy.Spider):
    name = "states"
    allowed_domains = ["city-data.com"]
    start_urls = [
        "http://www.city-data.com/indexes/schools/"
       
    ]  

    rate = 1 #maximum amount of pages downloaded in one sec
    def __init__(self): 
        self.download_delay = 1/float(self.rate)

    def parse(self, response):
        for href in response.css("ul.tab-list.tab-list-short > li > a::attr('href')"): 
        	url = response.urljoin(href.extract()) 
		yield scrapy.Request(url,callback=self.parse_tabs_links) 

    def parse_tabs_links(self,response):
	for href in response.css("ul.pagination.pagination-md > li > a::attr('href')"):
		url = response.urljoin(href.extract())
		yield scrapy.Request(url,callback=self.parse_tab_contents) 


    def parse_tab_contents(self,response): 
	state_name = response.xpath('//h1[@class="city"]/text()').extract()
	for sel in response.xpath('//table[@class="table"]/tbody/tr'): 
		item = SchoolItem()  
		item['name'] = sel.xpath('td[1]/a/text()').extract() 
		item['address']=sel.xpath('td[2]/text()').extract()
		item['rating']=sel.xpath('td[3]/text()').extract()
		item['enrollment']=sel.xpath('td[4]/text()').extract() 
		item['grade_span']=sel.xpath('td[5]/text()').extract()  
		item['state'] = state_name
		yield item				
        

