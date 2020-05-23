et= (input("insira a escala de temperatusa desejada C ou F: "))
t= float(input("insira a temperatura: "))
c=(5/9)*(t-32)
f=t/(5/9)+32
if et.upper()=="C":
	print(round(f,2))
if et.upper()=="F":
	print(round(c,2))
