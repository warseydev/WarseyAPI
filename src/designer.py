from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from langdetect import detect
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

def create(template, text, rgb1, rgb2, rgb3):
    deletetmp()
    width, height = (1024,1024)
    if rgb1 == None or rgb2 == None or rgb3 == None:
        rgbcolors = loadcolors(template)
        rgb1, rgb2, rgb3 = (rgbcolors["rgb1"], rgbcolors["rgb2"], rgbcolors["rgb3"])
    else:
        rgb1, rgb2, rgb3 = (int(rgb1), int(rgb2), int(rgb3))
    img = Image.open(f'designs/{template}.jpg')
    if detect(text) == "ar":
        myFont = ImageFont.truetype('arabic.ttf', 65)
    else:
        myFont = ImageFont.truetype('BebasNeue-Regular.ttf', 65)
    draw = ImageDraw.Draw(img)
    draw.text((width/2, 250), text, font=myFont, anchor="mm", fill =(rgb1, rgb2, rgb3))
    filename = randomword(12)
    img.save(f"tmp/{filename}.jpg", "JPEG")
    return filename
