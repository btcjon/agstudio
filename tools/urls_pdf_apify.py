# create a directory for pdfs if it doesn't exist
domain_name = base_url.split('//')[-1].replace('.', '_')
if not os.path.exists(domain_name):
    os.makedirs(domain_name)

# Initialize the ApifyClient with your API token
client = ApifyClient(APIFY_API_KEY)

# iterate over links, follow each one and convert to pdf
for link in links:
    page_url = base_url + link.get('href')
    if folder_path in page_url:
        try:
            # Prepare the Actor input
            run_input = {
                "url": page_url,
                "sleepMillis": 2000,
                "pdfOptions": { "format": "a4" },
            }

            # Run the Actor and wait for it to finish
            run = client.actor("WSjwXwzbDaPH2crYe").call(run_input=run_input)

            # Fetch and print Actor results from the run's dataset (if there are any)
            for item in client.dataset(run["defaultDatasetId"]).iterate_items():
                print(item)

            # Download the PDF and save it in the domain folder
            pdf_data = requests.get(item['pdfUrl']).content
            with open(domain_name + '/' + link.text + '.pdf', 'wb') as f:
                f.write(pdf_data)

        except Exception as e:
            print(f"Could not download {page_url}. Reason: {e}")
