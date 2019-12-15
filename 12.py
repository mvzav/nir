from PIL import Image
import pytesseract
import cv2
import pymysql

im="test1.jpg"
#img = Image.open(im)
preprocess="thresh"

im=cv2.imread(im)
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

elif preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)

filename = "urui.png"
cv2.imwrite(filename, gray)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open(filename),lang='rus')
#data=pytesseract .image_to_boxes(img)
print(text)
#print(data)

file=open("test.txt", 'w', encoding='utf-8')
file.write(text)

conn=pymysql.connect(host='localhost', user='root', password='', db='gramota',charset='utf8')
print(conn)
cursor=conn.cursor()
sql=f"INSERT INTO `gramota`.`test`(`zn`) VALUES ('{text}')"
print('sss')
print(sql)

cursor.execute(sql)
cursor.close()
conn.close()
