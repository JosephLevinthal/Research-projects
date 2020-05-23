# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
v = int(input(" Digite o valor: "))
print(" Entrada:",v)
if((v==2) or (v==5) or (v==10) or (v==20) or (v==50) or (v==100)):
	if(v==2):
		mensagem = "Tartaruga"
		print("Animal:",mensagem)
	elif(v==5):
		mensagem= "Garca"
		print("Animal:",mensagem)
	elif(v==10):
		mensagem= "Arara"
		print("Animal:",mensagem)
	elif(v==20):
		mensagem= "Mico-leao-dourado"
		print("Animal:",mensagem)
	elif(v==50):
		mensagem = " Onca-pintada "
		print("Animal:",mensagem)
	else:
		mensagem= "Garoupa"
		print("Animal:",mensagem)
else:
	mensagem= " Invalido "
	print("Animal:",mensagem)
		
		
	
			
	