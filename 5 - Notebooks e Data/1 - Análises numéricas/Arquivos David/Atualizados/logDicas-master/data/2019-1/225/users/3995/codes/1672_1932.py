x=float(input("distancia entre os olhos 1:"))
y=float(input("nariz e queixo1:"))
h=float(input("distancia entre os olhos 2:"))
i=float(input("nariz e queixo2:"))
w=float(input("distancia entre os olhos 3:"))
q=float(input("nariz e queixo3:"))
p1=(x/y)
p2=(h/i)
p3=(w/q)
if(abs(p1-p2)<=0.01):
	print(1, "e", 2)
elif(abs(p1-p3)<=0.01):
	print(1,"e",3)
elif(abs(p2-p3)<=0.01):
	print(2,"e",3)
