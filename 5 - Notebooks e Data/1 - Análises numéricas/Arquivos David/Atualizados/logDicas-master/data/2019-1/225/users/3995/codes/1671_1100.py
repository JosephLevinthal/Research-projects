# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
e=int(input("valor da nota:"))
print("Entrada:", e)
if((e==2) or (e==5) or (e==10) or (e==20) or (e==50) or (e==100)):
	if(e==2):
		msg="Tartaruga"
		print("Animal:",msg)
	elif(e==5):
		msg="Garca"
		print("Animal:",msg)
	elif(e==10):
		msg="Arara"
		print("Animal:",msg)
	elif(e==20):
		msg="Mico-leao-dourado"
		print("Animal:",msg)
	elif(e==50):
		msg="Onca-pintada"
		print("Animal:",msg)
	else:
		msg="Garoupa"
		print("Animal:",msg)
else:
	msg="Invalido"
	print("Animal:",msg)