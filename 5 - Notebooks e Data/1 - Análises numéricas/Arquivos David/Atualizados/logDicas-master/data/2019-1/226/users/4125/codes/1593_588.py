
valor = int(input("qual o valor do saque? "))

x = valor // 100
x50 = valor % 100
notas10 = x50 // 50
resto10 = x50 % 50
notas2 = resto10 // 10

print(int(x))
print(int(notas10))
print(int(notas2))


