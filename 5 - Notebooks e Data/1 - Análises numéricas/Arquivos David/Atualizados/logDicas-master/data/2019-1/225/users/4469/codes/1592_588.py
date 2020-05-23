saque = int(input("Valor a sacar: "))

notas100 = saque // 100

saque = saque - (notas100 * 100)

notas50 = saque // 50

saque = saque - (notas50 * 50)

notas10 = saque // 10

saque = saque - (notas10 * 10)

print(notas100)
print(notas50)
print(notas10)