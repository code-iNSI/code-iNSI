# Bilder müssen im gleichen Ordner wie das Script sein. Der QR-Code sollte zum Scannen etwas von der Kamera entfernt sein, da er sich sonst nicht scannen lässt.
from PIL import Image, ImageChops

bild1 = Image.open('image.png').convert('1')
bild2 = Image.open('image2.png').convert('1')

loesung = ImageChops.logical_xor(bild1, bild2)
loesung.save('loesung.png')
loesung.show()

