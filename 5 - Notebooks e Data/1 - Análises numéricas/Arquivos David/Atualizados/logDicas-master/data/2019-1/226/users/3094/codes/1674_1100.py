# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
c = int(input("valor: "))
x = "Animal: "
print("Entrada: ", c)

if(c == 2):
	y = Tartaruga
elif(c == 5):
	y = Garca
elif(c == 10):
	y = Arara
elif(c == 20):
	y = "Mico-leao-dourado"
elif(c == 50):
	y = "Onca-pintada"
elif(c == 100):
	y = "Garoupa"
else:
	y = "Invalido"
print("Animal:", y)