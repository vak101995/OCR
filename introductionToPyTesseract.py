import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_file = "data/page0.jpg"
no_noise = "temp/no_noise.jpg"

img = Image.open(no_noise)


ocr_result = pytesseract.image_to_string(img)

print(ocr_result)