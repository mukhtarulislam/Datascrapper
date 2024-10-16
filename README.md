# Web_content_extractor

# Data Scraper

A Python package to extract URLs from websites, extract content into DOCX files, and convert DOCX files to PDF.

## Features

- Extracts all href URLs from a specified website.
- Reads URLs from a CSV file and extracts specified HTML tags (h1, h2, p, span) into separate DOCX files.
- Converts DOCX files into PDF format.

## Requirements

- Python 3.x
- The following Python packages are required:
  - `requests`
  - `beautifulsoup4`
  - `python-docx`
  - `reportlab`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/data_scraper.git
   cd data_scraper


2.Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Install the required packages:
pip install -r requirements.txt



#Usage
Extract URLs to CSV
To extract URLs from a specified website and save them to a CSV file, use the extract_urls_to_csv function:

from data_scraper.url_extractor import extract_urls_to_csv

website_url = "https://example.com"  # Replace with your target website
folder_name = "output"  # Output folder for CSV
extract_urls_to_csv(website_url, folder_name)


#Extract Content from URLs
To read URLs from a CSV file and extract content into separate DOCX files, use the extract_content_from_urls function:


from data_scraper.content_extractor import extract_content_from_urls

urls = ["https://example.com/page1", "https://example.com/page2"]  # List of URLs
folder_name = "output"  # Output folder for DOCX files
extract_content_from_urls(urls, folder_name)

#Convert DOCX to PDF
To convert multiple DOCX files to PDF, use the convert_multiple_docx_to_pdf function:

from data_scraper.docx_to_pdf_converter import convert_multiple_docx_to_pdf

docx_folder = "output"  # Folder containing DOCX files
output_folder = "pdf_output"  # Output folder for PDF files
convert_multiple_docx_to_pdf(docx_folder, output_folder)

#License
This project is licensed under the MIT License. See the LICENSE file for details.


#Contributing
Contributions are welcome! Please follow these steps:

1.Fork the repository.

2.Create a new branch:
  git checkout -b feature/YourFeature
  
3.Make your changes and commit them:
  git commit -m "Add some feature"

4.Push to the branch:
  git push origin feature/YourFeature
  
5.Create a new Pull Request.

Contact
For questions or suggestions, please reach out to me Mukhtarulislam88@hotmail.com.
