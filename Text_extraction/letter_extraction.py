import pytesseract
import PIL.Image
import cv2


myconfig = r"--psm 3 --oem 3"
# text = pytesseract.image_to_string(PIL.Image.open("text.jpg"), config=myconfig)
# print(text)



img = cv2.imread("text.jpg")
height, weight, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
# print(boxes)

for box in boxes.splitlines():
    box = box.split(" ")
    img = cv2.rectangle(img, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0,255,0), 2 )

cv2.imshow("img", img)
cv2.waitKey(0)