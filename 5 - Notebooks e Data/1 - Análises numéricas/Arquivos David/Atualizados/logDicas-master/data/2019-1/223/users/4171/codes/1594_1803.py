n = int(input("Conta bancaria: "))

n1 = n // 1000 % 10  # primeiro digito
n2 = n // 100 % 10  # segundo digito
n3 = n // 10 % 10  # terceiro digito
n4 = n // 1 % 10  # quarto digito

somadig = (n1 * 5 + n2 * 4 + n3 * 3 + n4 * 2)
digver = somadig % 11

print(digver)
