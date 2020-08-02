from PIL import Image 
im=Image.open('myWriting.jpg')
ar=list(im.getdata())
print(ar)
cnt=0
idx=0
target=[0,1,0,1,0,1,0,1,0]

def dot(tup):
    if tup==(0,0,0):
        return 0
    if tup==(255,255,255):
        return 1

for a in ar:
    if dot(a)==target[idx]:
        print('found a match')
        cnt+=1
        idx+=1
    else:
        print('chain broken')
        cnt=0
        idx=0
if cnt==len(target):
    print('target found!')