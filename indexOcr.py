import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread("data/page0.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("temp/index_gray.png", gray)

blur = cv2.GaussianBlur(gray, (39,39), 0)

cv2.imwrite("temp/index_blur.png", blur)

thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite("temp/index_thresh.png", thresh)

