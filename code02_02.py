import cv2
import matplotlib.pyplot as plt

image_file = "data/image1.jpg"
img = cv2.imread(image_file)
cv2.imshow("Image", img)
cv2.waitKey(0)

def display (im_path):
    dpi = 80
    im_data = plt.imread(im_path)
    height,width = im_data.shape

    figsize = width / float(dpi), height / float(dpi)
    fig = plt.figure(figsize=figsize) 
    ax = fig.add_axes([0, 0, 1, 1])

    ax.axis('off')
    ax.imshow(im_data, camp = 'gray')
    plt.show()
 