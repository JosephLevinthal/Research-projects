valor = float(input("escreva o valor do saque: "))
notas50 = valor // 50
resto50 = valor % 50
notas10 = resto50 // 10
resto10 = resto50 % 10
notas2 = resto10 // 2

print(int(notas50))
print(int(notas10))
print(int(notas2))