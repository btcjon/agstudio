import requests
from xml.etree import ElementTree
from urllib.parse import urlparse
from collections import Counter
import argparse
import subprocess
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Process some URLs.')
parser.add_argument('domain', help='The domain to process')
args = parser.parse_args()

def print_sitemap_urls(domain):
    with open(f'tools/scraped/{domain}/urls.txt', 'r') as f:
        sitemap_url = f.readline().strip()

    response = requests.get(sitemap_url)
    tree = ElementTree.fromstring(response.content)

    # The namespace dictionary to target the 'loc' tags
    namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Find all 'loc' tags which contain the URLs
    urls = [url.text for url in tree.findall('.//ns:loc', namespaces)]

    # Save the URLs to a text file
    with open(f'tools/scraped/{domain}/individual_urls.txt', 'w') as f:
        for url in urls:
            f.write(url + '\n')

    # Initialize two Counter objects
    folder_counter = Counter()
    folder_combination_counter = Counter()

    for url in urls:
        # Parse the URL and extract the path
        path = urlparse(url).path

        # Split the path into folders
        folders = path.split('/')[1:]  # We start from 1 to ignore the first empty string

        # If there are folders in the path, increment the counter for the first folder
        if folders:
            folder_counter[folders[0]] += 1

        # If there are at least two folders in the path, concatenate them and increment the counter
        if len(folders) >= 2:
            folder_combination_counter[f'/{folders[0]}/{folders[1]}'] += 1

    # Print the count of URLs for each first-level folder
    print("First-level folder counts:")
    for folder, count in folder_counter.items():
        print(f'/{folder}: {count}')

    # Print the count of URLs for each first and second-level folder combination
    print("\nFirst and second-level folder combination counts:")
    for folder, count in folder_combination_counter.items():
        if count > 1:
            print(f'{folder}: {count}')
            
     # After printing the folder counts, ask the user for a list of folders to remove
    folders_to_remove = input("Enter a comma-separated list of folders to remove: ")

    # Split the user input into a list of folders
    folders_to_remove = [folder.strip() for folder in folders_to_remove.split(',')]

    # Read the URLs from the text file
    with open(f'tools/scraped/{domain}/individual_urls.txt', 'r') as f:
        urls = [line.strip() for line in f]

    # Filter out the URLs that contain any of the chosen folders
    urls = [url for url in urls if not any(folder in url for folder in folders_to_remove)]

    # Write the remaining URLs back to the text file
    with open(f'tools/scraped/{domain}/individual_urls.txt', 'w') as f:
        for url in urls:
            f.write(url + '\n')

    # Initialize two Counter objects
    folder_counter = Counter()
    folder_combination_counter = Counter()

    for url in urls:
        # Parse the URL and extract the path
        path = urlparse(url).path

        # Split the path into folders
        folders = path.split('/')[1:]  # We start from 1 to ignore the first empty string

        # If there are folders in the path, increment the counter for the first folder
        if folders:
            folder_counter[folders[0]] += 1

        # If there are at least two folders in the path, concatenate them and increment the counter
        if len(folders) >= 2:
            folder_combination_counter[f'/{folders[0]}/{folders[1]}'] += 1

    # Print the updated count of URLs for each first-level folder
    print("\nUpdated first-level folder counts:")
    for folder, count in folder_counter.items():
        print(f'/{folder}: {count}')

    # Print the updated count of URLs for each first and second-level folder combination
    print("\nUpdated first and second-level folder combination counts:")
    for folder, count in folder_combination_counter.items():
        if count > 1:
            print(f'{folder}: {count}')

# Use the function
print_sitemap_urls(args.domain)