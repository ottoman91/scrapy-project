import scrapy
from school.items import SchoolItem

class StateSpider(scrapy.Spider):
    name = "states"
    allowed_domains = ["city-data.com"]
    start_urls = [
        "http://www.city-data.com/indexes/schools/"
       
    ]

    def parse(self, response):
        for href in response.css("ul.tab-list.tab-list-short > li > a::attr('href')"): 
        	url = response.urljoin(href.extract()) 
		yield scrapy.Request(url,callback=self.parse_tab_contents) 


    def parse_tab_contents(self,response):
	for sel in response.xpath('//table[@class="table"]/tbody/tr'): 
		item = SchoolItem() 
		item['name'] = sel.xpath('td[1]/a/text()').extract() 
		item['address']=sel.xpath('td[2]/text()').extract()
		item['rating']=sel.xpath('td[3]/text()').extract()
		item['enrollment']=sel.xpath('td[4]/text()').extract() 
		item['grade_span']=sel.xpath('td[5]/text()').extract() 
		yield item				
        

