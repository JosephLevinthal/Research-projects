# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
x = int(input("valor da cedula:"))
#y = input("nome do animal:")
if(x==2):
	y = "Tartaruga"
elif(x==5):
	y = "Garca"
elif(x==10):
	y = "Arara"
elif(x==20):
	y = "Mico-leao-dourado"
elif(x==50):
	y ="Onca-pintada"
elif(x==100):
	y="Garoupa"
else:
	y = "Invalido"
print("Entrada:", x)
print("Animal:" , y)