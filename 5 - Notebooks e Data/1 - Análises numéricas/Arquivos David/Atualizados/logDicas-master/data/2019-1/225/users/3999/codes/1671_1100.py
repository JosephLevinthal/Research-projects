# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
x=int(input("Insira a Cedula: "))
print("Entrada:",x)
if(x!=100)and(x!=50)and(x!=20)and(x!=10)and(x!=5)and(x!=2):
	y="Invalido"
elif(x==100):
	y="Garoupa"
elif(x==50):
	y="Onca-pintada"
elif(x==20):
	y="Mico-leao-dourado"
elif(x==10):
	y="Arara"
elif(x==5):
	y="Garca"
elif(x==2):
	y="Tartaruga"
print("Animal:",y)	
