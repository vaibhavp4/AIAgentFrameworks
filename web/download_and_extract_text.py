# filename: download_and_extract_text.py

import requests
from PyPDF2 import PdfReader
from io import BytesIO

# URL of the PDF
url = "https://arxiv.org/pdf/2308.08155.pdf"

# Send a GET request
response = requests.get(url)

# Create a BytesIO object from the response content
content = BytesIO(response.content)

# Create a PDF file reader
reader = PdfReader(content)

# Initialize an empty string for the text
text = ""

# Loop through each page in the PDF
for page in reader.pages:
    # Add the text of the page to the string
    text += page.extract_text()

# Print the text
print(text)