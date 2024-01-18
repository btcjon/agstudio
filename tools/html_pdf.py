import os
import subprocess
import shutil

# specify the directory you want to start from
rootDir = '/Users/jonbennett/Downloads/us.sitesucker.mac.sitesucker/microsoft.github.io/autogen/docs'
pdfDir = os.path.join(rootDir, 'pdfs')

# create a directory for pdfs if it doesn't exist
if not os.path.exists(pdfDir):
    os.makedirs(pdfDir)

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname.endswith('.html'):
            print('\t%s' % fname)
            # get the parent directory name
            parent_dir_name = os.path.basename(dirName)
            # create the pdf file name
            pdf_file_name = parent_dir_name + '.pdf'
            pdf_path = os.path.join(dirName, pdf_file_name)
            # convert HTML to PDF with Pandoc
            subprocess.run(['pandoc', os.path.join(dirName, fname), '-s', '-o', pdf_path])
            # move the pdf to the main /docs folder, overwrite if exists
            destination_path = os.path.join(pdfDir, pdf_file_name)
            if os.path.exists(destination_path):
                os.remove(destination_path)
            shutil.move(pdf_path, pdfDir)