from pytesseract import image_to_string
from PIL import Image

im = Image.open(r'File_000.jpeg')
print(im)

print(image_to_string(im))
