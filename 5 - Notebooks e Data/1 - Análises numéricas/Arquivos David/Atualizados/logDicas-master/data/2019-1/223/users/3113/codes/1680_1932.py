a=float(input("distancia entre os olhos(face 1): "))
b=float(input("distancia entre o nariz e o queixo(face 1): "))
c=float(input("distancia entre os olhos(face 2): "))
d=float(input("distancia entre o nariz e o queixo(face 2): "))
e=float(input("distancia entre os olhos(face 3): "))
f=float(input("distancia entre o nariz e o queixo(face 3): "))

f1=a/b
s=round(f1,2)

f2=c/d
d=round(f2,2)

f3=e/f
w=round(f3,2)

c1=round(abs(s-d),2)
c2=round(abs(s-w),2)
c3=round(abs(d-w),2)
if(c1==0.01):
	print("1 e 3")
elif(c2:
	print("errado")
	