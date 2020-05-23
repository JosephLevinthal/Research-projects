
i1=float (input ("dist. entre os olhos da imagem 1: "))
y1=float (input ("dist. entre o nariz e o queixo im1: "))
i2=float (input ("dist. entre os olhos da imagem 2: "))
y2=float (input ("dist. entre o nariz e o queixo im2: "))
i3=float (input ("dist. entre os olhos da imagem 3: "))
y3=float (input ("dist. entre o nariz e o queixo im3: "))
f1=round (i1/y1,2)
f2=round (i2/y2,2)
f3=round (i3/y3,2)
x=abs (f1-f2)
y=abs (f1-f3)
z=abs (f2-f3)
if (x and y):
    print ("2 e 3")
elif (y and z):
    print ("1 e 2")
else:
    print ("1 e 3")
