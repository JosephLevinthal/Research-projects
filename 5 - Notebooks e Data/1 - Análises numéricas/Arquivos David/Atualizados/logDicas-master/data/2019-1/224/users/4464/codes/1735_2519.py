Atorre = int(input("insira a altura: "))
subindo = int(input("insira os minutos pra subir: "))
descendo = int(input("insira os minutos pra descer: "))

altura = subindo
tempo = 1

while(altura <= Atorre):
	altura = altura + subindo
	if (altura < Atorre):
		altura = altura - descendo
	tempo += 1
print(tempo)