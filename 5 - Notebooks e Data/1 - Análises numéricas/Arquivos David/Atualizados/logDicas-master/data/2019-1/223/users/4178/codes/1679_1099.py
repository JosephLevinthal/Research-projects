# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a= float(input("Valor A : "))
b= float(input("Valor B : "))
c= float(input("Valor C : "))
if (a > b + c or b > c + a or c > b + a): 
	msg = "invalido"
elif (a == b and b == c) :
	msg = "equilatero"
elif (a == b or b == c or c == a):
	msg = "isosceles"
else:
	msg = "escaleno"	
print("Entrada:",a, ",",b,",",c)
print("Tipo de triangulo:",msg)	