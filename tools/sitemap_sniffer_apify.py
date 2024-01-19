import argparse
from dotenv import load_dotenv
from apify_client import ApifyClient
import os
from urllib.parse import urlparse

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('APIFY_API_KEY')

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Process some URLs.')
parser.add_argument('url', help='The URL to process')
args = parser.parse_args()

# Initialize the ApifyClient with your API token
client = ApifyClient(api_key)

# Use the URL from the command-line arguments
run_input = {
    "url": args.url,
    "proxy": { "useApifyProxy": True },
}

# Run the Actor and wait for it to finish
run = client.actor("r6puf53mSCQGqJyN5").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
domain = urlparse(args.url).netloc  # Extract the domain from the URL
directory = f'tools/scraped/{domain}'
os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist

with open(f'{directory}/urls.txt', 'w') as f:
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        if item['statusCode'] == 200:
            f.write(item['url'] + '\n')
