import scrapy
from scrapy.crawler import CrawlerProcess

class SteamSpider(scrapy.Spider):
    name = "steam_spider"
    start_urls = ["https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s"]
    page = 1

    def parse(self, response):
        for link in response.css('div.search_results a::attr(href)'):
            yield response.follow(link, callback = self.parse_tags)
            for page in range(1, 43):
                next_page = f"https://store.steampowered.com/search/?filter=topsellers&page={page}"
                yield response.follow(next_page, callback = self.parse)
    
    def parse_tags(self, response):
            name = response.css("div.apphub_AppName::text").get()
            if name:
                yield {
                'name': name,
                'tags': list(map(str.strip, response.css(".app_tag::text").getall()))
            }

        
if __name__ == "__main__":
        process = CrawlerProcess(
        settings={
            "FEEDS": {
                "steam_tags.csv": {"format": "csv"},
            },
        }
    )


process.crawl(SteamSpider)
process.start()
