import os
import pdfkit
import requests

def convert_url_to_pdf(url, output_dir):
    # Save the page as PDF
    pdf_path = os.path.join(output_dir, url.split('/')[-1] + '.pdf')
    pdfkit.from_url(url, pdf_path)

# Usage
convert_url_to_pdf('https://example.com', '/path/to/output/directory')