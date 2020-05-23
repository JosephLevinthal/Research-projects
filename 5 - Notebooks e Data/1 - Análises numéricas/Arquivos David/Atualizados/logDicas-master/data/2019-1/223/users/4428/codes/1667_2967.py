altura1 = float(input("Digite sua altura: "))
altura2 = float(input("Digite a altura do acompanhante: "))

if(altura1 >= 1.37):
	mensagem = "sim"
	
if(altura2 >= 1.37):
	mensagem = "Sim"
	
else:
	mensagem = "Nao"
print (mensagem)
print (max(altura1, altura2))