import os
from PIL import Image

IMAGE_FIT_WIDTH, IMAGE_FIT_HEIGHT = 300,225
LOGO_FILENAME = './Pictures/ArtI_Logo.png'

logo = Image.open(LOGO_FILENAME, 'r')
logoWidth, logoHeight = logo.size
print(logoWidth, logoHeight)
lh = int(IMAGE_FIT_HEIGHT*0.1)
lw = int(lh/float(logoHeight)*logoWidth)
print(lw,lh)
logo = logo.resize((lw,lh))

#Looping over all the files in the directory
os.makedirs('withLogo')
for filename in os.listdir('.'):
    if not(filename.endswith('.png') or filename.endswith('.jpg')) or filename==LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size
    print("Resizing image ",filename)
    im = im.resize((IMAGE_FIT_WIDTH, IMAGE_FIT_HEIGHT))
    # Adding the logo
    print("Pasting logo on image ", filename)
    im.paste(logo,(IMAGE_FIT_WIDTH-lw, IMAGE_FIT_HEIGHT-lh), logo)
    im.save(os.path.join('withLogo', filename))



