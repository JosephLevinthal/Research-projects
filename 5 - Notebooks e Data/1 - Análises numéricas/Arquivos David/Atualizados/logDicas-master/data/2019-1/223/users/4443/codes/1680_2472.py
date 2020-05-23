# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
q1 = input("Digite a alternativa da q1 (a, b, c, d, ou e): ")
q2 = input("Digite a alternativa da q2 (a, b, c, d, ou e): ")
q3 = input("Digite a alternativa da q3 (a, b, c, d, ou e): ") 
g1 = input("Digite o gabarito da q1 (a, b, c, d, ou e): ")
g2 = input("Digite o gabarito da q2 (a, b, c, d, ou e): ")
g3 = input("Digite o gabarito da q3 (a, b, c, d, ou e): ")
pts = 0
if(q1 == g1):
	pts = pts + 1
if(q2 == g2):
	pts = pts + 1
if(q3 == g3):
	pts = pts + 1
print(pts)	