# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a1 = float(input("digite o valor de a:"))
b2 = float(input("digite o valor de b:"))
c3 = float(input("digite o valor de c:"))
if (a1> 0 and b2> 0 and c3> 0):	
	if(a1+b2 > c3 and b2+c3 > a1 and a1+c3 > b2 ): 
		if(a1 == b2  == c3):
			print("Entrada:" , a1 , ",", b2 , ",", c3)