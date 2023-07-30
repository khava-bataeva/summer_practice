import scrapy
from scrapy.crawler import CrawlerProcess


class SteamSpider(scrapy.Spider):
    name = 'steam_tags'
    allowed_domains = ["store.steampowered.com"]
    url = "https://store.steampowered.com/search/?category1=998&filter=topsellers&ndl=1&page=%s"
    page = 1
    start_urls = [url % page]
    count = 0

    def parse(self, response):
        for el in response.css('div.search_results a::attr(href)'):
            yield response.follow(el, callback=self.tags)
        if self.count < 1000:
            self.page += 1
            yield response.follow(self.url % self.page, callback=self.parse)

    def tags(self, response):
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
                "tags.csv": {"format": "csv"},
            },
        }
    )

    process.crawl(SteamSpider)
    process.start()
