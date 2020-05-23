x=float(input("acai no copo: "))
s=int(input("salgados: "))
v=float(input("valor pago em dinheiro: "))
x1=x*24/1000
y1=s*3
t=x1+y1
print(round(t,2))
if(v>x1+y1):
	print("Sim")
else:
	print("Nao")
