QiV = int(input("copias do virus no sangue de Micaleteia: ")) 
QiL = int(input("insira a quantidade de leuzinhos no sangue: "))
percentualV = float(input("insira o percy da multi de virus diario: "))
percentualL = float(input("insira o percy da multi de leuzinho diarios"))

V = QiV
L = QiL
dias = 0

while (L < 2*V):
	V = V + ((V*percentualV)/100)
	L = L + ((L*percentualL)/100)
	dias = dias + 1
print(dias)