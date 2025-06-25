import time

class ETALogger:
    def __init__(self, logger, estimated_total_pages=None, log_interval=2):
        self.logger = logger
        self.estimated_total_pages = estimated_total_pages
        self.log_interval = log_interval
        self.pages_scraped = 0
        self.start_time = None

    def start(self):
        self.start_time = time.time()
        self.pages_scraped = 0
        self.logger.info("ETA Logger started.")

    def log_progress(self):
        self.pages_scraped += 1
        if self.pages_scraped % self.log_interval == 0:
            elapsed = time.time() - self.start_time
            rate = self.pages_scraped / elapsed if elapsed > 0 else 0
            if self.estimated_total_pages:
                remaining = self.estimated_total_pages - self.pages_scraped
                eta = remaining / rate if rate > 0 else float('inf')
                self.logger.info(f"Scraped {self.pages_scraped}/{self.estimated_total_pages} pages in {elapsed:.1f}s (rate: {rate:.2f} pages/s, ETA: {eta:.1f}s)")
            else:
                self.logger.info(f"Scraped {self.pages_scraped} pages in {elapsed:.1f}s (rate: {rate:.2f} pages/s)")

    def finish(self):
        elapsed = time.time() - self.start_time
        self.logger.info(f"ETA Logger finished. Total pages scraped: {self.pages_scraped} in {elapsed:.1f}s.")
