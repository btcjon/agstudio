import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.parse import urlsplit
import os
import argparse
import time
import sys

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

# Read URLs from file
with open(os.path.join(file_dir, 'urls.txt'), 'r') as f:
    urls = f.read().splitlines()

# Extract unique main folders
main_folders = set()
for url in urls:
    path = urlsplit(url).path
    # Split the path to get the main folder
    parts = path.split('/')
    if len(parts) > 2:  # Changed from 1 to 2
        main_folder = '/' + parts[1] + '/' + parts[2]  # Added parts[2]
        main_folders.add(main_folder)

# Print unique main folders
print("The following main folders were found:")
for folder in sorted(main_folders):
    print(folder)

# Check if script is running in interactive mode
if sys.stdin.isatty():
    # Ask user for folders to remove
    folders_to_remove = input("Enter the folders to remove, separated by commas (leave empty if none): ").split(',')

    # If user provided input, proceed with removal
    if folders_to_remove[0] != '':
        # Remove leading/trailing whitespace from each folder
        folders_to_remove = [folder.strip() for folder in folders_to_remove]

        # Filter URLs to exclude those that contain any of the folders to remove
        urls = [url for url in urls if not any(folder in url for folder in folders_to_remove)]

        # Write remaining URLs back to file
        with open(os.path.join(file_dir, 'urls.txt'), 'w') as f:
            for url in urls:
                f.write(f"{url}\n")

        print(f"Removed URLs containing {', '.join(folders_to_remove)}. {len(urls)} URLs remain in {os.path.join(file_dir, 'urls.txt')}.")
    else:
        print("No folders were removed.")
