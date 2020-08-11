from PIL import Image 
im=Image.open('myWriting.jpg')
ar=list(im.getdata())
print(ar)
cnt=0
idx=0

im2=Image.open('target.jpg')
target=list(im2.getdata())
target_x=im2.width
target_y=im2.height


#let's iterate over the image in terms of x and y:
img_x=im.width
img_y=im.height
print(img_x,img_y)#check
#how many time we can move small image in large image? largeX-smallx+1
#need to show table that worked it out.
for x in range(img_x-target_x+1):
    for y in range(img_y-target_y+1):
        print(f"x:{x},y:{y}")
        # and the position of the pixel in ar will be y*width+x
        print(f"currently looking at pixel :{ar[y*img_x+x]}")
        # we are looking for a pattern, so we need to compare the target pattern from here.
        #counter for pixels found, if found all then we have a matching pattern.
        foundFlag=True
        for tx in range(target_x):
            for ty in range(target_y):
                print(x+tx,' ', y+ty)
                print('target pixel:',target[ty*target_y+tx])
                print('img_pixel:',ar[(y+ty)*img_x+(x+tx)])
                if target[ty*target_y+tx]==ar[(y+ty)*img_x+(x+tx)]:
                    print('match found:',ar[(y+ty)*img_x+(x+tx)])
                else:
                    #only switch to false when not found.
                    foundFlag=False
                    print('no match, skip to next...')
                    break
        if foundFlag==True:
            print('found a pattern at:',x,y)
    

