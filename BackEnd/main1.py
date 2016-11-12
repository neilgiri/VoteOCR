import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

image = Image.open(r'Top_half.png')
image = image.filter(ImageFilter.MinFilter(1))

#Increasing Contrast
contrast = ImageEnhance.Contrast(image)
image = contrast.enhance(50)

#Making Picture Black+White
color = ImageEnhance.Color(image)
image = color.enhance(0.0)

#Increasing Brightness
bright = ImageEnhance.Brightness(image)
image = bright.enhance(5.0)

#Increasing Sharpness
sharpness = ImageEnhance.Sharpness(image)
image = sharpness.enhance(5.0)

#Printing translation
print(pytesseract.image_to_string(image))
