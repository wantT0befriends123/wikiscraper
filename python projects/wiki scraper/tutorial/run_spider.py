import os

json_path = os.path.join(os.path.dirname(__file__), 'pages.json')
if os.path.exists(json_path):
    os.remove(json_path)

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())
process.crawl('wiki')
process.start()