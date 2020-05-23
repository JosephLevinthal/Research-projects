# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
q1= input("insira a resposta 1: ").lower()
q2= input("insira a resposta 2: ").lower()
q3= input("insira a resposta 3: ").lower()
g1= input("insira a resposta g1: ").lower()
g2= input("insira a resposta g2: ").lower()
g3= input("insira a resposta g3: ").lower()
if (q1==g1):
	a1=1
if (not(q1==g1)):
	a1=0
if(q2==g2):
	a2=1
if(not(q2==g2)):
	a2=0
if(q3==g3):
	a3=1
if(not(q3==g3)):
	a3=0
r=(a1+a2+a3)
print(r)




