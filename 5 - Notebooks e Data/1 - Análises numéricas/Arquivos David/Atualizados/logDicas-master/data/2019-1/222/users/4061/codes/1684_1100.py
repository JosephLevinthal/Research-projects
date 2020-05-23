# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
cedula = int(input("digite cedula: "))

print("Entrada: ", cedula)
				 
if(cedula == 2):
	mensagem = "Tartaruga"
elif(cedula == 5):
	mensagem = "Garca"
elif(cedula == 10):
	mensagem = "Arara"
elif(cedula == 20):
	mensagem = "Mico-leao-dourado"
elif(cedula == 50):
	mensagem = "Onca-pintada"
elif(cedula == 100):
	mensagem = "Garoupa"
else:
	mensagem = "Invalido"


print("Animal: " , mensagem)
				 

