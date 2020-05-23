# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a=float(input("lado1:"))
b=float(input("lado2:"))
c=float(input("lado3:"))
print("Entradas:", a, ",", b, ",", c)
if(a>0 and b>0 and c>0):
	if(a>=b+c or b>=a+c or c>=a+b):
		msg="invalido"
	else:
		if(a==b and b==c):
			msg="equilatero"
		else:
			if(a==b or a==c or b==c):
				msg="isosceles"
			else:
				msg="escaleno"
else:
	msg="invalido"
print("Tipo de triangulo:",msg)
