capacidade = int(input("Capacidade do navio: "))
estoque = int(input("Estoque inicial: "))
q = int(input("Quantidade: "))
				
semana = 1

while(estoque > 0):
	q = q * semana
	estoque = (estoque - capacidade) + q
	semana = semana + 1
	
	 
print(semana)	