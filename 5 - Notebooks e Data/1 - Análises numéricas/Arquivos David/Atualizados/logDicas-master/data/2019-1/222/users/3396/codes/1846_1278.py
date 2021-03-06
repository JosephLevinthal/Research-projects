from numpy import*
saida = int(input("Cidade de saida: "))
destino = int(input("Cidade de destino: "))

soma_do_tempo = 0

matriz = array([[0, 2, 11, 6, 15, 11, 1],
			 [2, 0, 7, 12, 4, 2, 15],
			 [11, 7, 0, 11, 8, 3, 13],
			 [6, 12, 11, 0, 10, 2, 1],
			 [15, 4, 8, 10, 0, 5, 13],
			 [11, 2, 3, 2, 5, 0, 14],
			 [1, 15, 13, 1, 13, 14, 0]])

while (saida != -1 and destino != -1):
	# Indexando os as entradas tirando somente o último número
	# Por exemplo, se a saida for 555, então o i será 5, mas como na matriz 555
	# indica o índice 4, subtraimos 1 do resultado
	
	i = (saida%10) - 1
	j = (destino%10) - 1
	
	# Atualizando a soma do tempo
	soma_do_tempo = soma_do_tempo + matriz[i, j]
	
	# Como nosso destino tornou-se nossa nova saida, atualizaremos a saida (nova) para ser igual ao destino(antigo)
	saida = destino
	destino = int(input("Cidade de destino: "))
	
print(soma_do_tempo)