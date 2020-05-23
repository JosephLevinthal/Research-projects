var = int(input("digite os 4 digitos da sua conta bancaria (nao iremos rouba-lo): "))
d1 = var//1000%100%10
d2 = var//100%10
d3 = var//10%10
d4 = var%10
soma = d4 * 2 + d3 * 3 + d2 * 4 + d1 * 5
digito_v = soma%11
print(digito_v)

