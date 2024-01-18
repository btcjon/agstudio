import os
import pdfkit
import requests

# Path to the text file
text_file_path = 'tools/scrape/microsoft.github.io-docs-urls.txt'

# Read the URLs from the text file
with open(text_file_path, 'r') as f:
    urls = f.read().splitlines()

# Extract the website name from the first URL
website_name = urls[0].split('/')[2] if urls else ''

# Create a directory for the PDFs
pdf_dir = os.path.join(os.path.dirname(text_file_path), f'{website_name}_{os.path.basename(text_file_path).split(".")[0]}_pdfs')
os.makedirs(pdf_dir, exist_ok=True)

# Create a file for logging errors
error_log_path = os.path.join(pdf_dir, 'errors.txt')

# Iterate over the URLs
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        with open(error_log_path, 'a') as error_log:
            error_log.write(f"Error occurred with URL {url}: {e}\n")
        continue  # Skip this URL and continue with the next one

    # Save the page as PDF
    pdfkit.from_url(url, os.path.join(pdf_dir, url.split('/')[-1] + '.pdf'))