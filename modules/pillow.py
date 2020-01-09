from PIL import Image,ImageFilter

image = Image.open("kus.jpg")
#image.show()
image.save("kus2.jpg")

image.rotate(180).save("kus3.jpg")
image.convert(mode = "L").save("kus4.jpg")

changeSize = (960,600)
image.thumbnail(changeSize)
image.save("kus6.jpg")

#Effects
image.filter(ImageFilter.GaussianBlur(10)).save("kus8.jpg")


image2 = Image.open("atatürk.jpg")
#edit
edit_size = (340,0,950,600)
image2.crop(edit_size).save("atam1.jpg")