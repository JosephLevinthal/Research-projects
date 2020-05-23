from numpy import*

P = array(eval(input())) #massa
H = array(eval(input())) #altura

V = zeros(size(P), dtype=float)
for i in range(size(P)):
	IMC = round((P[i]/(H[i] * H[i])), 2)
	V[i] = V[i] + IMC
	
if (max(V) < 17):
	S = "MUITO ABAIXO DO PESO"
elif (max(V) >= 17 and max(V) <= 18.49):
	S = "ABAIXO DO PESO"
elif (max(V) >= 18.5 and max(V) <= 24.99):
	S = "PESO NORMAL"
elif (max(V) >= 25 and max(V) <= 29.99):
	S = "ACIMA DO PESO"
elif (max(V) >= 30 and max(V) <= 34.99):
	S = "OBESIDADE"
elif (max(V) >= 35 and max(V) <= 39.99):
	S = "OBESIDADE SEVERA"
elif (max(V) >= 40):
	S = "OBESIDADE MORBIDA"
print(V)
print("O MAIOR IMC DA TURMA EH: ", max(V))
print(S)
