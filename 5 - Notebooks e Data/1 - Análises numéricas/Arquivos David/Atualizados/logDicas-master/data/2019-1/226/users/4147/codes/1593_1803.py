numero = float(input("Digite um numero de quatro digitos: "))
a = numero // 1000
a1 = numero % 1000
b = a // 100
b1 = a % 100
c = b // 10
c1 = b % 10
d = c1
s = ((a * 5) + (b * 4) + (c * 3) + (d * 2))
print(s % 11)