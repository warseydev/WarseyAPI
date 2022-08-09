from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import random, string
import os, json

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def deletetmp():
    for f in os.listdir("tmp"):
        os.remove(os.path.join("tmp", f))

def loadcolors(template):
    f = open('designs/config.json')
    config = json.load(f)
    try: 
        rgb1 = config[template][0]["rgb1"]
        rgb2 = config[template][0]["rgb2"]
        rgb3 = config[template][0]["rgb3"]
    except:
       rgb1, rgb2, rgb3 = (255, 255, 255)
    colors = {"rgb1": rgb1, "rgb2": rgb2, "rgb3": rgb3}
    return colors

def checkarabic(text):
	if "غ" in text or "ظ" in text or "ص" in text or "ق" in text or "ر" in text or "ش" in text or "ت" in text or "ث" in text or "خ" in text or "ذ" in text or "ض" in text or "ح" in text or "ط" in text or "ي" in text or "ك" in text or "ل" in text or "م" in text or "ن" in text or "س" in text or "ع" in text or "ف" in text or "ب" in text or "ج" in text or "و" in text or "د" in text or "ه" in text or "ء" in text or "ا‎" in text:
		return True
	else:
		return False

def create(template, text, rgb1, rgb2, rgb3):
    deletetmp()
    width, height = (1024,1024)
    if rgb1 == None or rgb2 == None or rgb3 == None:
        rgbcolors = loadcolors(template)
        rgb1, rgb2, rgb3 = (rgbcolors["rgb1"], rgbcolors["rgb2"], rgbcolors["rgb3"])
    else:
        rgb1, rgb2, rgb3 = (int(rgb1), int(rgb2), int(rgb3))
    img = Image.open(f'designs/{template}.jpg')
    if checkarabic(text):
        myFont = ImageFont.truetype('arabic.ttf', 50)
        text = arabic_reshaper.reshape(text)
        text = get_display(text)   
    else:
        myFont = ImageFont.truetype('BebasNeue-Regular.ttf', 65)
    draw = ImageDraw.Draw(img)
    draw.text((width/2, 250), text, font=myFont, anchor="mm", fill =(rgb1, rgb2, rgb3))
    filename = randomword(12)
    img.save(f"tmp/{filename}.jpg", "JPEG")
    return filename
