from PIL import Image,ImageFilter

image = Image.open("kucuk1_17.jpg")
changeSize = (642,640)
image.thumbnail(changeSize)
image.save("kucuk1_17yenix.jpg")

