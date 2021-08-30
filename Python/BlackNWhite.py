from PIL import Image
im = Image.open('./Modi.png','r')
w, h = im.size
print("Width of image is : ", w)
print("Height of image is : ", h)
im_bw = Image.new("RGBA", (w,h))
for x in range(w):
    for y in range(h):
        val = sum(im.getpixel((x,y)))/4         #Alternate formula = 0.3*R + 0.59*G + 0.11*B
        im_bw.putpixel((x,y),(val,val,val,255))
im_bw.save('Modi1.png')
print('Image saved successfully!')
im.convert('LA').save('./Pictures/zzz1.png')