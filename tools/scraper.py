import argparse
import subprocess
from urllib.parse import urlparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Process some URLs.')
parser.add_argument('url', help='The URL to process')
args = parser.parse_args()

def main(url):
    domain = urlparse(url).netloc  # Extract the domain from the URL

    # Run sitemap_sniffer_apify.py
    subprocess.run(['python', 'tools/sitemap_sniffer_apify.py', url])

    # Run process_sitemap_urls_for_selection.py
    subprocess.run(['python', 'tools/process_sitemap_urls_for_selection.py', domain])

# Use the function
main(args.url)