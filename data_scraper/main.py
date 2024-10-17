import argparse
import os
from data_scraper.url_extractor import extract_urls_to_csv, extract_content_from_urls
from data_scraper.docx_to_pdf_converter import DocxToPdfConverter, convert_multiple_docx_to_pdf


def main():
    parser = argparse.ArgumentParser(description="Data Scraper Utility")
    
    # Add arguments
    parser.add_argument('--url', type=str, help="URL of the website to scrape", required=False)
    parser.add_argument('--csv_folder', type=str, help="Folder to save the URLs CSV", required=False)
    parser.add_argument('--docx_folder', type=str, help="Folder to save the extracted DOCX files", required=False)
    parser.add_argument('--pdf_folder', type=str, help="Folder to save the converted PDF files", required=False)
    parser.add_argument('--action', type=str, choices=['extract_urls', 'extract_content', 'convert_to_pdf'], 
                        help="Action to perform: extract_urls, extract_content, convert_to_pdf", required=True)
    
    # Parse arguments
    args = parser.parse_args()

    # Handle actions based on the user's input
    if args.action == 'extract_urls':
        if args.url and args.csv_folder:
            # Extract URLs and save to CSV
            extract_urls_to_csv(args.url, args.csv_folder)
        else:
            print("For extracting URLs, please provide both --url and --csv_folder")
    
    elif args.action == 'extract_content':
        if args.csv_folder and args.docx_folder:
            # Read URLs from the CSV and extract content into DOCX
            csv_file = os.path.join(args.csv_folder, 'urls.csv')
            if os.path.exists(csv_file):
                with open(csv_file, 'r') as f:
                    urls = [line.strip() for line in f]
                extract_content_from_urls(urls, args.docx_folder)
            else:
                print(f"No CSV file found at {csv_file}")
        else:
            print("For extracting content, please provide both --csv_folder and --docx_folder")
    
    elif args.action == 'convert_to_pdf':
        if args.docx_folder and args.pdf_folder:
            # Convert DOCX files to PDF
            convert_multiple_docx_to_pdf(args.docx_folder, args.pdf_folder)
        else:
            print("For converting to PDF, please provide both --docx_folder and --pdf_folder")


if __name__ == "__main__":
    main()
