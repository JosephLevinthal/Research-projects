idade = int(input("informe sua idade: "))

if (idade >= 18):
	msg = "eleitor"
else: 
	msg = "nao_eleitor"
	
print(msg.lower())