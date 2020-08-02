#search for one world in a sentence!
data='i have an apple in my appreciation bag!'
target='apple'

cnt=0
idx=0
for c in data:
    print('now looking at:',c)
    if c==target[idx]:
        print('found a match:',c)
        idx+=1
        cnt+=1
    else:
        print('chain broken')
        idx=0
        cnt=0
    if cnt==len(target):
        print('world found!')
        break


            