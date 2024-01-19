import os
import subprocess

def convert_pdf_to_md(pdf_path, output_dir):
    # Check if the file is a PDF
    if pdf_path.endswith('.pdf'):
        # Convert the PDF to markdown
        output_path = os.path.join(output_dir, os.path.basename(pdf_path)[:-4] + '.md')
        subprocess.run(['python', 'tools/marker/convert_single.py', pdf_path, output_path])

# Usage
convert_pdf_to_md('/path/to/file.pdf', '/path/to/output/directory')