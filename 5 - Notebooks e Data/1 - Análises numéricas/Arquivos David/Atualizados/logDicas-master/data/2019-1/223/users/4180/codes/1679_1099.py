# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída


a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
print("Entradas:",a,",",b,",",c)

if((a >= b+c) or (b >= a+c) or (c >= a+b)):
	
	print("Tipo de triangulo: invalido ")
	
elif((a == b)and(b == c)):
	
   print("Tipo de triangulo: equilatero")
	
elif ((a==b)or(b==c)or(c==a)):
	
	print("Tipo de triangulo: isosceles")
	
elif ((a!= b)and(b!= c)and(c!= a)):
	
	print("Tipo de triangulo: escaleno")
	
else:
	
	print("Tipo de triangulo: invalido")
		
   
				
	
	
		
		
			