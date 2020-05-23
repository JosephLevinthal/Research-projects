v =input("digite escala da temperatura: ")
x =int(input("digite a quantidade de temperatura: "))


if v.upper() == "F":
	F = (5/9)*(x-32)
	print(round(F,2))

if v.upper() == "C":
	C = ((9/5)*x) +32 
	print(round(C,2))