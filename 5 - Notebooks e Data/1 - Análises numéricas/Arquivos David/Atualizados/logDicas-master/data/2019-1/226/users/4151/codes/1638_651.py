x=float(input("altura: "))
y=input("sexo(M ou F)")

if(y.upper()=="M"):
	print(round(72.7*x-58,2))
else:
	print(round(62.1*x-44.7,2))