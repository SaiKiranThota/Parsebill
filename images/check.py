from PIL import Image ,ImageFilter ,ImageEnhance
import pytesseract

im =Image.open("temp.png" )
text = pytesseract.image_to_string(im ,lang='eng')
p=[]
q=[]
z=[]
text = (text).split()
print(text)
for i in range(7,len(text)):
    if (i%3==0 ):
        p.append(text[i])
    elif (i%3==1):
        q.append(text[i])
    else :
        z.append(text[i])
for i in range( 0 ,len(q)-1):
    print(i,"product" ,q[i])
for i in range( 0 ,len(z)-1):
    print(i,"product" ,z[i])
print ('total price' ,p[-1])

    
