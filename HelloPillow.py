# Simply creates a new 1920x1920 image that says "Hello Pillow!"
from PIL import Image, ImageFont, ImageDraw

image = Image.new('RGBA', (1920, 1920),"black")
message = "Hello World!"
font = ImageFont.truetype("arial.ttf", 75)
w,h = font.getsize(message)
draw = ImageDraw.Draw(image)

# Parameter list in order:
# The bounds of the image, the message being written, the color of the text, the font, and the spacing.
draw.text(((1920-w)/2,(1920-h)/2),message,fill="white",font=font,spacing=10)

image.show()
