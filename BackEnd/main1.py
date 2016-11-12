import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

image = Image.open(r'File_000.jpeg')
image = image.filter(ImageFilter.MedianFilter())
enhance = ImageEnhance.Contrast(image)
image = enhance.enhance(2)
image = image.convert('1')
print(pytesseract.image_to_string(image))
