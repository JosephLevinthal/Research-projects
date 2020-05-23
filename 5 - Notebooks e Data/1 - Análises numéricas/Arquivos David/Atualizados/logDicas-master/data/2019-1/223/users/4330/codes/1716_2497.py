V=float(input("Valor: "))
QMA=int(input("Tempo de investimento(quantidade de meses de aplicacao): "))
Tempo = 0
while( Tempo < QMA ):
		Lucro = V * 0.04
		V = V + Lucro
		Tempo = Tempo + 1
		print(round(V, 2))
