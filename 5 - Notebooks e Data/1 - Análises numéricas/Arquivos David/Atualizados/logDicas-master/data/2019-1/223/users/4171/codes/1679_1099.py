# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (a == b == c):
	t = "equilatero"
if (a == b and a != c or b == c and b != a or c == a and c != b):
	t = "isosceles"
if (a != b and b != c and c != a):
	t = "escaleno"
if (a < 0 or b < 0 or c < 0) or (a > b + c) or (b > a + c) or (c > a + b):
	t = "invalido"
print("Tipo de triangulo: ", t)
