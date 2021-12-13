from PIL import Image, ImageChops

bild1 = Image.open('image.png').convert('1')
bild2 = Image.open('image2.png').convert('1')

loesung = ImageChops.logical_xor(bild1, bild2)
loesung.save('loesung.png')
loesung.show()

