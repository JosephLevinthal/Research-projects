percurso = float(input("escreva o percurso da viagem: "))
opcao = input("escreva qual o tipo de carro? (A/B): ")
if (opcao == "A"):
	consumo = percurso /8
else:
	consumo = percurso /12
print(round(consumo, 2))