import os
import subprocess

# Directory containing the PDFs
pdf_dir = 'tools/scrape/microsoft.github.io_microsoft_pdfs'

# Iterate over all files in the directory
for filename in os.listdir(pdf_dir):
    # Check if the file is a PDF
    if filename.endswith('.pdf'):
        # Full path to the PDF
        pdf_path = os.path.join(pdf_dir, filename)
        
        # Convert the PDF to markdown
        output_path = os.path.join(pdf_dir, filename[:-4] + '.md')
        subprocess.run(['python', 'tools/marker/convert_single.py', pdf_path, output_path])