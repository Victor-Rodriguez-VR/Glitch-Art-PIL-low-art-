from PIL import Image, ImageFilter
import sys

try:
    image = Image.open("May_De_Bae.jpg")
except IOError:
    print("File was not found")
    sys.exit(1)
blurred = image.filter(ImageFilter.BLUR)
blurred.show()