# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = input().lower()
b = input().lower()
c = input().lower()
A = input().lower()
B = input().lower()
C = input().lower()

contador = 0

if(a == A):
	contador = contador + 1

if(b == B):
	contador = contador + 1
	
if(c == C):
	contador = contador + 1

print(contador)