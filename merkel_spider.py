import scrapy

class MerkelSpider(scrapy.Spider):
    name = "merkel_spider"
    start_urls = [ 
'https://www.bundeskanzlerin.de/bkin-de/aktuelles/70298!search?formState=eNptjz0PgjAQhv-KuZkBSNTYDT921NE41HKtJNBie6iE8N89NOji9t7led7L9VBIwoO0BgOIHpZxukrHoL2rQdi2qiIg90nDEIGWCumLLkCcYJ1nxwZRXeHMQCNNaSWVzo6Qdw-Gk3kEgaQnEDEjTuuANLXfWvTdNFROvd39v2VWX0raltxkFYKANAa-5zGE3R0tbfgT435acONBwOfoNJXssNgyMiswKBZV6z1buTTclQwvGmZakA&limit=800'
    ]        
    def parse_speech(self, response):
        xpath_content = '#main div div.basepage_pages p::text'
        c = response.css(xpath_content).extract()
        c = " ".join(c)
        print(c)
        
    def parse(self, response):
        xpath_speech = '#searchResult li h3 a::attr(href)'
        for searchResult in response.css(xpath_speech).getall():
            speach = response.urljoin(searchResult)
            yield scrapy.Request(speach, callback=self.parse_speech)
            
