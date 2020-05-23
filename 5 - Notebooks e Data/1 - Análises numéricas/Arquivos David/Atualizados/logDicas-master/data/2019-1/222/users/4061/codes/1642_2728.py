percurso = float(input("digite percurso: "))
tipo = input("digite tipo: ")

A = 8
B = 12

if(tipo=="A"):
	mensagem = percurso / A 
else:
	mensagem = percurso / B
	
print(round(mensagem, 2))
