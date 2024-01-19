import argparse
import subprocess
from urllib.parse import urlparse
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Process some URLs.')
parser.add_argument('url', help='The URL to process')
args = parser.parse_args()

def main(url):
    domain = urlparse(url).netloc  # Extract the domain from the URL

    print("Starting the scraping process...")
    # Run sitemap_sniffer_apify.py
    subprocess.run(['python', 'tools/sitemap_sniffer_apify.py', url])

    print("Running process_sitemap_urls_for_selection.py...")
    # Run process_sitemap_urls_for_selection.py
    subprocess.run(['python', 'tools/process_sitemap_urls_for_selection.py', domain])

    # Convert each URL to a PDF
    pdf_output_dir = f'tools/scraped/{domain}/pdfs'
    os.makedirs(pdf_output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    with open(f'tools/scraped/{domain}/individual_urls.txt', 'r') as f:
        urls = [line.strip() for line in f]

    print("Converting URLs to PDFs...")
    # Run url_2_pdf.py
    subprocess.run(['python', 'tools/url_2_pdf.py', *urls, pdf_output_dir])

    # Convert PDFs to Markdown
    md_output_dir = f'tools/scraped/{domain}/md'
    os.makedirs(md_output_dir, exist_ok=True)  # Create the directory if it doesn't exist

    print("Converting PDFs to Markdown...")
    # Run marker_pdf_md.py
    subprocess.run(['python', 'tools/marker_pdf_md.py', pdf_output_dir, md_output_dir])

    print("Scraping process completed successfully.")

# Use the function
main(args.url)