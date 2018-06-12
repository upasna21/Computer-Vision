from PIL import Image
import pytesseract

img = Image.open("Epo Automation Content.jpeg")
text = pytesseract.image_to_string(img,lang='eng')

print(text)
