# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("equilatero"))
b = float(input("isosceles"))
c = float(input("escaleno"))

 if((a >= b + c) or (b >= a + c) or (c >= a + b)):
	
	else:
		if((a == b) and (b == c)):
			print("equilatero")
		else:
			if((a == b) or (b ==c) or (c == a)):
				print("isosceles")
			else:
				print("escaleno")
				
		
	