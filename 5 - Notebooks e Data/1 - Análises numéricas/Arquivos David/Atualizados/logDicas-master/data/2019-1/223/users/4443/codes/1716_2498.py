# definicao das variaveis para coleta das entradas
ha = int(input("Numero de habitantes de uma cidade A: "))
hb = int(input("Numero de habitantes de uma cidade B: "))
ca = float(input("Percentual de crescimento de uma cidade A: "))
cb = float(input("Percentual de crescimento de uma cidade B: "))

t = 0 #acumula o tempo transcorrido em anos

while(ha <= hb): #condicao do laco: hab cidade a inferior ao da cidade b
	ha = ha + (ha*ca/100) #crescimento populacional cidade a
	hb = hb + (hb*cb/100) #crescimento populacional cidade b
	t = t+1 #incremento no tempo
print(t) #impressao 