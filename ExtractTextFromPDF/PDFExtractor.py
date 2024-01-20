import re
import pdfplumber

class PDFExtractor:
    def extract_information_from_pdf(self, pdf_path):
        # Function to extract text from PDF using pdfplumber
        def extract_text_with_pdfplumber(pdf_path):
            text = ''
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text()
            return text

        # Define regular expressions for extracting information
        product_name_pattern = re.compile(r"Product Name\s*:\s*(.*)", re.IGNORECASE)
        seller_pattern = re.compile(r"Seller\s*:\s*(.*)", re.IGNORECASE)
        price_pattern = re.compile(r"Price\s*:\s*(\d+)", re.IGNORECASE)
        action_pattern = re.compile(r"Action\s*:\s*(.*)", re.IGNORECASE)

        # Extract text from the PDF
        extracted_text = extract_text_with_pdfplumber(pdf_path)

        # Extract information using regex
        product_name_match = product_name_pattern.search(extracted_text)
        seller_match = seller_pattern.search(extracted_text)
        price_match = price_pattern.search(extracted_text)
        action_match = action_pattern.search(extracted_text)

        product_name = product_name_match.group(1) if product_name_match else None
        seller = seller_match.group(1) if seller_match else None
        price = int(price_match.group(1)) if price_match else None
        action = action_match.group(1) if action_match else None

        # Return a list of extracted values
        return [product_name, seller, price, action]
