import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import argparse
import time

def crawl_website(url, base_url, visited=None, counter=[0]):
    if visited is None:
        visited = set()

    visited.add(url)

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: The server returned a {response.status_code} status code for URL {url}")
        return []

    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')

    links = soup.find_all('a')
    urls_in_directory = []

    for link in links:
        href = link.get('href')
        if href:
            if '#' in href or '?' in href:
                continue

            absolute_href = urljoin(base_url, href)

            if urlparse(absolute_href).netloc != urlparse(base_url).netloc:
                continue

            if absolute_href.startswith(base_url):
                urls_in_directory.append(absolute_href)

            if absolute_href not in visited and absolute_href.startswith(base_url):
                try:
                    response = requests.get(absolute_href)
                    if response.status_code == 200:
                        counter[0] += 1
                        if counter[0] % 5 == 0:
                            print(f"Crawled {counter[0]} URLs so far...")
                        urls_in_directory.extend(crawl_website(absolute_href, base_url, visited, counter))
                    time.sleep(0.5)  # Rate limiting
                except requests.exceptions.RequestException as e:
                    print(f"Error: Failed to crawl URL {absolute_href}: {e}")

    return urls_in_directory

parser = argparse.ArgumentParser(description='Crawl a website and save all URLs to a text file.')
parser.add_argument('url', help='The URL of the website to crawl.')
args = parser.parse_args()

base_url = args.url
urls = crawl_website(base_url, base_url)

urls = list(set(urls))

domain_name = urlparse(base_url).netloc
file_dir = os.path.join('tools', 'scrape', domain_name)
os.makedirs(file_dir, exist_ok=True)

with open(os.path.join(file_dir, 'urls.txt'), 'w') as f:
    for url in urls:
        f.write(f"{url}\n")

print(f"Saved {len(urls)} URLs to {os.path.join(file_dir, 'urls.txt')}")

# Extract unique subdirectories
subdirectories = set()
for url in urls:
    path = urlparse(url).path
    subdirectory = '/' + path.split('/')[1] + '/'
    if subdirectory:
        subdirectories.add(subdirectory)

print("The following subdirectories saved:")
for subdirectory in subdirectories:
    print(subdirectory)