import cv2
import pytesseract

image = cv2.imread('gramota/ishodny/Blag_Zav.jpg')
custom_config = r'--oem 3 --psm 6'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR5\tesseract.exe'
text = pytesseract.image_to_string(image, config=custom_config, lang='rus')
print(text)

