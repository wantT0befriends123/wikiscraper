from pathlib import Path
from .eta_logger import ETALogger

#scrapy crawl quotes -O quotes.json
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    estimated_total_pages = 10  # Set this to your estimated total number of pages

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eta_logger = ETALogger(self.logger, estimated_total_pages=self.estimated_total_pages, log_interval=10)
      
    def start_requests(self):
        self.eta_logger.start()
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.eta_logger.log_progress()
        for quote in response.css("div.quote"):
            yield {
                "url": response.url,
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)