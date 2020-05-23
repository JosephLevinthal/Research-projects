a=float(input("valor: "))
b=int(input("quantidade: "))
c=float(input("valor dos tickets: "))
d=int(input("quantidade de passes: "))
e=float(input("valor dos passes: "))

if a>(b*c)+(d*e):
	print("SUFICIENTE")

else:
    print("INSUFICIENTE")