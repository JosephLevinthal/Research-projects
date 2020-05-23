
valor = int(input("Qual o valor do saque? "))
x = valor // 50 
x50 = valor % 50
notas10 = x50 // 10
resto10 = x50 % 10
notas2 = resto10 // 2

print(int(x))
print(int(notas10))
print(int(notas2))
