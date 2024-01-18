import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import pdfkit

def crawl_website(url, base_url, folder_path, visited=None):
    if visited is None:
        visited = set()

    # Add url to set of visited pages
    visited.add(url)

    # Send a GET request
    response = requests.get(url)

    # If the GET request is not successful, print an error message and return an empty list
    if response.status_code != 200:
        print(f"Error: The server returned a {response.status_code} status code for URL {url}")
        return []

    # Get the content of the response
    page_content = response.content

    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find all the links in the webpage
    links = soup.find_all('a')

    # List to store all urls within specified directory
    urls_in_directory = []

    # Iterate over links, check if they are within specified directory
    for link in links:
        href = link.get('href')
        if href:
            # Ignore links with URL parameters or fragments
            if '#' in href or '?' in href:
                continue

            # If link is relative, convert it to absolute
            absolute_href = urljoin(base_url, href)

            # Ignore links to other domains
            if urlparse(absolute_href).netloc != urlparse(base_url).netloc:
                continue

            if folder_path in absolute_href:
                urls_in_directory.append(absolute_href)

            # If the link has not been visited, crawl it
            if absolute_href not in visited and base_url in absolute_href:
                try:
                    # Check if the page exists before crawling
                    response = requests.get(absolute_href)
                    if response.status_code == 200:
                        urls_in_directory.extend(crawl_website(absolute_href, base_url, folder_path, visited))
                except requests.exceptions.RequestException as e:
                    print(f"Error: Failed to crawl URL {absolute_href}: {e}")

    return urls_in_directory

# Usage
base_url = 'https://microsoft.github.io/autogen/'
folder_path = '/docs/'
urls = crawl_website(base_url, base_url, folder_path)

# Remove duplicates
urls = list(set(urls))

# Create a directory for the PDFs
pdf_dir = os.path.join('tools/scrape', 'pdfs')
os.makedirs(pdf_dir, exist_ok=True)

# PDFKit options
options = {
    'page-size': 'Letter',
    'orientation': 'Portrait',
    'no-background': None,
    'zoom': 1,
    'grayscale': None,
}

# Iterate over the URLs
for url in urls:
    # Save the page as PDF
    pdfkit.from_url(url, os.path.join(pdf_dir, url.split('/')[-1] + '.pdf'), options=options)
