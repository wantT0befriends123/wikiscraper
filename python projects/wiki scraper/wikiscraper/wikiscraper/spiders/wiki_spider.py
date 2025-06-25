from pathlib import Path
from .eta_logger import ETALogger
from urllib.parse import urlparse
import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = [
        "https://en.wikipedia.org/wiki/Wikipedia"
    ]
    estimated_total_pages = 5000  # Set this to your estimated total number of pages

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.eta_logger = ETALogger(self.logger, estimated_total_pages=self.estimated_total_pages, log_interval=10)
      
    def start_requests(self):
        self.eta_logger.start()
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.eta_logger.log_progress() # Log progress after each page is parsed
        relative_url = urlparse(response.url).path # Extract the relative URL path
        # Count all links on the page
        all_links = response.css('a::attr(href)').getall()
        num_all_links = len(all_links)
        # Extract all article links: start with /wiki/ and do not contain ':'
        article_links = response.css('a::attr(href)').re(r'^/wiki/[^:]+$')
        # Only follow non-stub article links
        non_stub_article_links = [link for link in article_links if 'stub' not in link.lower()]

        yield {
            "url": relative_url, # Use the relative URL path
            "title": response.css('span.mw-page-title-main::text').get(), # Extract the title from the page
            "num_links": num_all_links # Number of all links on the page
            #"links": all_links, # List of all links on the page
        }

        yield from response.follow_all(non_stub_article_links, callback=self.parse)