# docx_to_pdf_converter.py

from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def convert_docx_to_pdf(docx_file, pdf_file):
    """
    Converts a .docx file to a PDF file using ReportLab.

    Args:
        docx_file (str): The path to the .docx file to be converted.
        pdf_file (str): The path where the PDF will be saved.

    Returns:
        None
    """
    # Load the .docx document
    doc = Document(docx_file)

    # Create a new PDF canvas
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter
    y = height - 40  # Start at the top of the page

    # Iterate through paragraphs in the .docx file
    for para in doc.paragraphs:
        if not para.text.strip():  # Skip empty paragraphs
            continue

        # Set font size and style based on the paragraph style (header or normal text)
        if para.style.name == 'Heading 1':
            c.setFont("Helvetica-Bold", 14)
        elif para.style.name == 'Heading 2':
            c.setFont("Helvetica-Bold", 12)
        else:
            c.setFont("Helvetica", 10)

        # Start a new page if the current page is full
        if y < 40:  
            c.showPage()
            y = height - 40

        # Draw the paragraph text on the PDF
        c.drawString(40, y, para.text)
        y -= 14  # Adjust spacing for next line

    # Save the PDF file
    c.save()

def convert_multiple_docx_to_pdf(docx_folder, output_folder):
    """
    Converts all .docx files in a folder to PDF files.

    Args:
        docx_folder (str): The folder containing .docx files to be converted.
        output_folder (str): The folder where the converted PDF files will be saved.

    Returns:
        None
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through .docx files in the input folder and convert each to PDF
    for filename in os.listdir(docx_folder):
        if filename.endswith('.docx'):
            docx_file = os.path.join(docx_folder, filename)
            pdf_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.pdf")
            convert_docx_to_pdf(docx_file, pdf_file)
            print(f"Converted {docx_file} to {pdf_file}")
