import os
import subprocess
import argparse
import glob

def convert_pdf_to_md(pdf_dir, output_dir):
    for filename in os.listdir(pdf_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_dir, filename)
            md_path = os.path.join(output_dir, filename[:-4] + '.md')
            subprocess.run(['python', 'tools/marker/convert_single.py', pdf_path, md_path])

    # Delete JSON files
    for json_file in glob.glob(os.path.join(output_dir, '*.json')):
        os.remove(json_file)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Convert PDFs to Markdown.')
parser.add_argument('pdf_dir', help='The directory containing the PDFs')
parser.add_argument('output_dir', help='The directory to save the Markdown files')
args = parser.parse_args()

# Use the function
convert_pdf_to_md(args.pdf_dir, args.output_dir)