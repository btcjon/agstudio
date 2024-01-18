import os
import pdfkit
import requests

# Path to the text file
text_file_path = 'tools/scrape/microsoft.github.io-docs-urls.txt'

# Read the URLs from the text file
with open(text_file_path, 'r') as f:
    urls = f.read().splitlines()

# Create a directory for the PDFs
pdf_dir = os.path.join(os.path.dirname(text_file_path), 'pdfs')
os.makedirs(pdf_dir, exist_ok=True)

# Iterate over the URLs
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        continue  # Skip this URL and continue with the next one

    # Save the page as PDF
    pdfkit.from_url(url, os.path.join(pdf_dir, url.split('/')[-1] + '.pdf'))