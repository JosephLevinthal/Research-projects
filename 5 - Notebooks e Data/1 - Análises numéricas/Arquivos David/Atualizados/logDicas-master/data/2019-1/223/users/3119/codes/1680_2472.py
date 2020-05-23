# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

R = input("Digite as resposta do aluno: ")
R1 = input("Digite as resposta do aluno: ")
R2 = input("Digite as resposta do aluno: ")
Q = input("Digite o gabarito: ")
Q1 = input("Digite o gabarito: ")
Q2 = input("Digite o gabarito: ")

soma = 0
if(R == Q):
	soma = soma + 1
if(R1 == Q1):
	soma = soma + 1
if(R2 == Q2):
	soma = soma + 1
	
print(soma)
	