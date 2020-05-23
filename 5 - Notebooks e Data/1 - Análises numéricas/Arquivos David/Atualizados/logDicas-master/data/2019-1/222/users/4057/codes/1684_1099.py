# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
A = float(input ("Lado 1: "))
B = float(input ("Lado 2: "))
C = float(input ("Lado 3: "))
D = A + B
E = B + C
F = A + C
print("Entradas:", A, ",", B, ",", C)

if (A == B) and (B == C)and (A == C) :
	X = "equilatero"
	print("Tipo de triangulo: ", X)
elif ((A == B) and (B != C) and (A != C)) or ((A == C) and (B != C) and (A != B)) or ((A != C) and (B == C) and (A != B)):
	X = "isosceles"
	print("Tipo de triangulo: ", X)
elif (A != B) and (B != C) and (A != C) and((D > C)and (E>A)and(F>B)) :
	X = "escaleno"
	print("Tipo de triangulo: ", X)
else: 
	X = "invalido"
	print("Tipo de triangulo: ", X)