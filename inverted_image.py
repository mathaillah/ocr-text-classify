import cv2


inverted_image = cv2.bitwise_not(cv2.imread("data/image1.jpg"))
cv2.imwrite("temp/inverted_image.jpg", inverted_image)
