import os
import pdfkit
import argparse
from PyPDF2 import PdfMerger  # Change this line

def convert_url_to_pdf(urls, output_dir):
    for url in urls:
        # Save the page as PDF
        pdf_path = os.path.join(output_dir, url.split('/')[-1] + '.pdf')
        pdfkit.from_url(url, pdf_path)

    print("Combining PDFs...")
    merger = PdfMerger()  # Change this line

    for pdf in os.listdir(output_dir):
        if pdf.endswith('.pdf'):
            merger.append(os.path.join(output_dir, pdf))

    merger.write(os.path.join(output_dir, 'ALL.pdf'))
    merger.close()
    print("PDFs combined successfully.")

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Convert URLs to PDFs.')
parser.add_argument('urls', nargs='+', help='The URLs to convert')
parser.add_argument('output_dir', help='The directory to save the PDFs')
args = parser.parse_args()

# Use the function
convert_url_to_pdf(args.urls, args.output_dir)