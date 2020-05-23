p = int(input("digite quantos pirarucu no tanque: "))
p1 = float(input("percentual de crescimento: "))

t = 0
#8000 pirarucu

while(0<p<8000):
	x = int(input("quantidade retirada: "))
	p  = p + (p1/100)*p - x
	t = t + 1
if(p<=0):
	print("Zero".upper())
	print(t)
elif(p>=8000):
	print("maximo".upper())
	print(t)