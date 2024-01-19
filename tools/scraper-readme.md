# Web Scraper

This script is designed to scrape a website for URLs, convert the pages at those URLs to PDFs and/or Markdown files, and save them in a structured directory. 

## How It Works

1. The script uses the BeautifulSoup library to parse the HTML of the website and find all the links. It only considers links that are within the specified folders (if any).

2. The script then uses the pdfkit library to convert the pages at the found URLs to PDFs, and a subprocess call to a script named convert_single.py to convert the PDFs to Markdown files.

3. For each URL, the script creates a directory under "tools/scrape" with the name of the domain. Inside this directory, it creates two subdirectories: one for the PDFs and one for the Markdown files. It also creates a text file to save the URLs and an error log file.

4. The script uses argparse to handle command-line arguments. The user can specify whether they want to convert the URLs to PDFs and/or Markdown files by using the -pdf and -md flags respectively. 

5. The user can also specify a folder to restrict the crawling to by using the -f flag, and whether to combine the processed files into one by using the -c flag.

## Example Usage
bash
python tools/scraper.py https://docs.retool.com/ -pdf -md -c -f apps,workflows,ai


This command will scrape the website at "https://docs.retool.com/", but only within the "apps", "workflows", and "ai" directories. It will convert the pages to PDFs and Markdown files, and save them in the respective directories under "tools/scrape/docs.retool.com". 

The URLs will be saved in a text file named "docs.retool.com-urls.txt", and any errors that occur during the process will be logged in a file named "errors.txt".

If the -c flag is used, the script will also combine all the PDF files into a single file named "docs.retool.com_ALL.pdf" and all the Markdown files into a single file named "docs.retool.com_ALL.md".