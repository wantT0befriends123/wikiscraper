import subprocess
import sys
import os

# Run the spider
print("Running the Scrapy spider...")
spider_proc = subprocess.run([sys.executable, 'run_spider.py'], cwd=os.path.dirname(__file__))
if spider_proc.returncode != 0:
    print("Spider failed. Exiting.")
    sys.exit(1)

# Run the analysis
print("Running the analysis script...")
analysis_proc = subprocess.run([sys.executable, 'analyze_pages.py'], cwd=os.path.dirname(__file__))
if analysis_proc.returncode != 0:
    print("Analysis failed.")
    sys.exit(1)

print("All done!")
