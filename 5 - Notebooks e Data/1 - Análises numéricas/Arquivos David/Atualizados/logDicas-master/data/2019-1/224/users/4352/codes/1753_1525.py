vi = int(input("digite o volume inicial de agua na masmorra: "))
vab = int(input("digite o volume de agua bombardeado: "))
var = int(input("digite o volume retirado da masmorra: "))
acum = 0
cont = 0
final = (vi + vab) - var
while final <= 1000:
	final = (vi + vab) - var
	acum = (acum + final) / 36
	cont = cont + 1
print(cont)