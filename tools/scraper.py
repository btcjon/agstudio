import os
import pdfkit
import requests
import subprocess
import warnings
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import argparse

# Ignore XML parse warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

def crawl_website(url, visited=None):
def crawl_website(url, visited=None, folders=None):
    if visited is None:
        visited = set()
    if folders is None:
        folders = args.folder

    base_url = url

    # Add url to set of visited pages
    visited.add(url)

    # Send a GET request
    response = requests.get(url)
    time.sleep(1)  # Add a delay of 1 second between requests

    # If the GET request is not successful, print an error message and return an empty list
    if response.status_code != 200:
        with open(error_log_path, 'a') as error_log:
            error_log.write(f"Error: The server returned a {response.status_code} status code for URL {url}\n")
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

            # Add the absolute href to the list of URLs to be processed later
            urls_in_directory.append(absolute_href)

    # Print the number of URLs found
    print(f"Crawled {url}, found {len(urls_in_directory)} URLs so far.")

    # Recursively crawl the URLs that have not been visited
    for absolute_href in urls_in_directory:
        if absolute_href not in visited and base_url in absolute_href:
            try:
                # Check if the page exists before crawling
                response = requests.get(absolute_href)
                time.sleep(1)  # Add a delay of 1 second between requests
                if response.status_code == 200:
                    urls_in_directory.extend(crawl_website(absolute_href, visited, folders))
            except requests.exceptions.RequestException as e:
                with open(error_log_path, 'a') as error_log:
                    error_log.write(f"Error: Failed to crawl URL {absolute_href}: {e}\n")

    return urls_in_directory

                urls_in_directory.append(absolute_href)

                # Write the URL to the file
            with open(text_file_path, 'a') as f:
                f.write(f"{absolute_href}\n")

                # If the link has not been visited and is within the base URL, crawl it
                if absolute_href not in visited and base_url in absolute_href:
                    try:
                        # Check if the page exists before crawling
                        response = requests.get(absolute_href)
                        time.sleep(1)  # Add a delay of 1 second between requests
                        if response.status_code == 200:
                            urls_in_directory.extend(crawl_website(absolute_href, visited))
                    except requests.exceptions.RequestException as e:
                        with open(error_log_path, 'a') as error_log:
                            error_log.write(f"Error: Failed to crawl URL {absolute_href}: {e}\n")

    print(f"Crawled {url}, found {len(urls_in_directory)} URLs so far.")
    return urls_in_directory

# Create the parser
parser = argparse.ArgumentParser(description='Process some URLs.')

# Add the arguments
parser.add_argument('urls', metavar='URLs', type=str, nargs='+',
                    help='the URLs to process')
parser.add_argument('-pdf', '--pdf', action='store_true',
                    help='convert the URLs to PDFs')
parser.add_argument('-md', '--markdown', action='store_true',
                    help='convert the URLs to Markdown files')

def format_folder(s):
    folders = [item.strip() for item in s.split(',')]
    folders = [('/' + folder + '/') if not folder.startswith('/') and not folder.endswith('/') else folder for folder in folders]
    return folders

parser.add_argument('-f', '--folder', type=format_folder, default='',
                    help='the folders to restrict crawling to')
parser.add_argument('-c', '--combine', action='store_true',
                    help='combine the processed files into one')

# Parse the arguments
args = parser.parse_args()

print("Getting stop words...")
stop_words = input("Enter any stop words, separated by commas: ").split(',')
stop_words = [word.strip() for word in stop_words]
# Parse the arguments
args = parser.parse_args()

print("Scraping URLs...")
all_urls = []
for url in args.urls:
    all_urls.extend(crawl_website(url))

# Filter URLs based on specified folders
if args.folder:
    all_urls = [url for url in all_urls if any(urlparse(url).path.startswith(folder) for folder in args.folder)]

print("Getting stop words...")
stop_words = input("Enter any stop words, separated by commas: ").split(',')
stop_words = [word.strip() for word in stop_words]

# Filter URLs based on stop words
all_urls = [url for url in all_urls if not any(word in url for word in stop_words)]

# Process the URLs
for url in all_urls:
    # Extract the domain name from the base URL
    parsed_uri = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    ...
    print("Processing URLs...")
    # Iterate over the URLs
    processed_files = {'md': [], 'pdf': []}
    for url in urls:
        try:
            if args.pdf:
                # Save the page as PDF
                pdf_path = os.path.join(pdf_dir, url.split('/')[-1] + '.pdf')
                pdfkit.from_url(url, pdf_path, options=options)
                processed_files['pdf'].append(pdf_path)

            if args.markdown:
                # Convert the PDF to markdown
                output_path = os.path.join(md_dir, url.split('/')[-1] + '.md')
                subprocess.run(['python', 'tools/marker/convert_single.py', pdf_path, output_path])
                processed_files['md'].append(output_path)
        except requests.exceptions.RequestException as e:
            with open(error_log_path, 'a') as error_log:
                error_log.write(f"Error occurred with URL {url}: {e}\n")

    # Combine the processed files into one
    if args.combine:
        for filetype, files in processed_files.items():
            if files:
                combined_filename = f"{domain.replace('.', '_')}_ALL.{filetype}"
                with open(os.path.join(domain_dir, combined_filename), 'w') as outfile:
                    for fname in files:
                        with open(fname) as infile:
                            outfile.write(infile.read())
                            outfile.write("\n\n")
print("All done!")