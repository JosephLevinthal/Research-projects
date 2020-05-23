qi = float(input("digite o qi de copias: "))
qi2 = float(input("digite a qi2 de leucocitos: "))
p1 = float(input("digite o percentual de multiplicacao diaria do virus: "))
p2 = float(input("digite o percentual de multiplicacao diaria de leucocitos: "))


dia = 0
while(2*qi>=qi2):
	qi = qi*(1 + (p1/100))
	qi2 = qi2*(1 + (p2/100))
	dia = dia + 1
print(dia)