valor = int(input("Qual o valor do saque? "))

x = valor // 100
x1 = valor % 100

y = x1 // 50
y1 = x1 % 50

z = y1 // 10

print(int(x))
print(int(y))
print(int(z))