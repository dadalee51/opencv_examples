#looking for image in image.
from PIL import Image 
im=Image.open('myWriting.jpg')
img_x=im.width
img_y=im.height
ar=list(im.getdata())
print('ar looks like:',ar)

im2=Image.open('target.jpg')
target_x=im2.width
target_y=im2.height
target=list(im2.getdata())
print('target looks like:',target)

for x in range(img_x-target_x+1):
    for y in range(img_y-target_y+1):
        foundFlag=True
        for tx in range(target_x):
            for ty in range(target_y):
                if target[ty*target_x+tx]!=ar[(y+ty)*img_x+(x+tx)]:
                    foundFlag=False
                    break
        if foundFlag==True:
            print('found a pattern at:',x,y)
    

