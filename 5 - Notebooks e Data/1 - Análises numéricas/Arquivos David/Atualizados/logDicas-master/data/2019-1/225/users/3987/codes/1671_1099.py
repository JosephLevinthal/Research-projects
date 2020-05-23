# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

print("Entradas:", a, ",", b, ",", c)

#invalido
if(abs(b-c)<a<(b+c)):
   if ((a == b) and (b == c) and (a == c)):
	   print("Tipo de triangulo:", "equilatero")
   else:
      if ((a == b) or (b == c)):
	      print("Tipo de triangulo:", "isosceles")
      else:
	      print("Tipo de triangulo:", "escaleno")
else:
	print("Tipo de triangulo:", "invalido")
				
				
			   