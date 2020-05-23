# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
c= float(input())
x= float(input())
f= float(input())

print("Entradas: ", c ,", " ,x, ",",f)
if(f>=c+x) or (c>=x+f) or (x>=c+f):
	print("Tipo de triangulo: invalido")
elif (c==x) and (x==f):
	print("Tipo de triangulo: equilatero")
elif (c==x) or (x==f) or (c==f):
	print ("Tipo de triangulo: isosceles")
else:
	print ("Tipo de triangulo: escaleno")
	