# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A=float(input("lado A :"))
B=float(input("Lado B: "))
C=float(input("Lado C: "))
print("Entradas:",A,",",B,",",C)
if(A==B==C):
	X="equilatero"
elif(A>=B+C)or(B>=A+C)or(C>=A+B):
	X="invalido"
elif(A==B)or(C==B):
	X="isosceles"
else:
	X="escaleno"
print("Tipo de triangulo: ",X)	