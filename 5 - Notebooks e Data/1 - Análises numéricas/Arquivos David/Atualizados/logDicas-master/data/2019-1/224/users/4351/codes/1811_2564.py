from numpy import*
golspro= array(eval(input("vetor de gols efetuado pelo time do iferno : ")))
golscont= array(eval(input("vetor de gols contra: ")))
i = 0
vitoria=0
empate= 0
derrota= 0
for v in golspro:
	if (golspro[i]>golscont[i]):
		vitoria= vitoria + 1
		i = i + 1
	elif (golspro[i]==golscont[i]):
		empate= empate + 1
		i = i + 1
	elif (golspro[i]<golscont[i]):
		derrota= derrota + 1
		i = i + 1
resultados= zeros(3, dtype=int)
resultados[0]=vitoria
resultados[1]=empate
resultados[2]=derrota
print(resultados)