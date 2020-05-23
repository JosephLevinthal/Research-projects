valor_a = int(input("valor a "))
valor_b = int(input("valor b "))
valor_c = int(input("valor c "))

minimo = min(valor_a,valor_b,valor_c)
maximo = max(valor_a,valor_b,valor_c)
mediano = valor_a + valor_b + valor_c - minimo - maximo

print(minimo)
print(mediano)
print(maximo)