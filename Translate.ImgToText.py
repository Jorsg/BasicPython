import pytesseract
from PIL import Image

# Set the image file path
image_file_path = 'C:\\Users\\Admin\\testOCR.jpg'

# Open the image file
with Image.open(image_file_path) as image:
    # Perform OCR on the image
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Admin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(image)

    # Print the OCR result
    print(text)