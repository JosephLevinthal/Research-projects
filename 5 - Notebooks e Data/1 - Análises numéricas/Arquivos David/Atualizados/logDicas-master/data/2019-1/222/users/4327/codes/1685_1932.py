#imageem 1
do1=float(input("dstancia entre os olhos: "))
dn1=float(input("dstancia entre onariz e o queixo: "))
#imageem 2
do2=float(input("dstancia entre os olhos: "))
dn2=float(input("dstancia entre onariz e o queixo: "))
#imageem 3
do3=float(input("dstancia entre os olhos: "))
dn3=float(input("dstancia entre onariz e o queixo: "))

#calculo das faces 
fc1=do1/dn1
fc2=do2/dn2
fc3=do3/dn3
#diferencas das imagens
x=abs(fc1-fc2)
y=abs(fc1-fc3)
z=abs(fc2-fc3)

if ((x and y) < x):
	print ("1 e 2")
elif ( (x and z) < y):
	print ("1 e 3")
elif ( (z and y) < x):
	print ("2 e 3")


