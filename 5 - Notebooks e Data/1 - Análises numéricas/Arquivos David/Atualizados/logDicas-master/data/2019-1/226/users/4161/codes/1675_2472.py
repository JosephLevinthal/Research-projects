# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
n1 = input("questao 1: ").lower()
n2 = input("questao 2: ").lower()
n3 = input("questao 3: ").lower() 
g1 = input("resposta 1: ").lower()
g2 = input("resposta 1: ").lower()
g3 = input("resposta 1: ").lower() 
if n1 == g1:
	a = 1
else:
	a = 0
if n2 == g2:
	b = 1
else:
	b = 0
if n3 == g3:
	c = 1
else:
	c = 0
print(a+b+c)