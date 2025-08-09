from PIL import Image

im_file = "data/image1.jpg"

im = Image.open(im_file)
im.save("temp/image1.jpg")