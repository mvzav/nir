import cv2
import numpy as np
import pytesseract

#получение изображения в оттенках серого
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#удаление шума
def remove_noise(image):
    return cv2.medianBlur(image,5) #что за число

#определение порога
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#расширение
def dilate(image):
    kernel = np.ones((5,5),np.unit8)
    return cv2.dilate(image, kernel, iterations= 1)

#эрозия
def erode(image):
    kernel = np.ones((5, 5), np.unit8)
    return cv2.erode(image, kernel, iterations=1)

#открытие эрозия с последующим расширением
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#край обнаружения
def canny(image):
    return cv2.Canny(image, 100, 200)

#коррекция перекоса
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#соответсвие шаблону
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


image = cv2.imread('gramota/my_scann/1.jpg')

gray = get_grayscale(image)
filename = "gramota/my_scann/1_gray.jpg"
cv2.imwrite(filename, gray)

thresh = thresholding(gray)
filename = "gramota/my_scann/1_thresh.jpg"
cv2.imwrite(filename, thresh)

opening = opening(gray)
filename = "gramota/my_scann/1_opening.jpg"
cv2.imwrite(filename, opening)

canny = canny(gray)
filename = "gramota/my_scann/1_canny.jpg"
cv2.imwrite(filename, canny)

#добавление пользовательских параметров
custom_config = r'--oem 3 --psm 6'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR5\tesseract.exe'
text = pytesseract.image_to_string(image, config=custom_config, lang='rus')
print(text)