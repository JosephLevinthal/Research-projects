# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
var1 = int(input("Entrada: "))

if var1 == 2:
	msg="Tartaruga"
elif var1 == 5:
	msg="Garca"
elif var1 == 10:
	msg="Arara"
elif var1 == 20:
	msg="Micro-leao-dourado"
elif var1 == 50:
	msg="Onca-pintada"
elif var1 == 100:
	msg="Garoupa"
else:
	msg="Invalido"
print("Entrada:", var1)
print("Animal:", msg)
