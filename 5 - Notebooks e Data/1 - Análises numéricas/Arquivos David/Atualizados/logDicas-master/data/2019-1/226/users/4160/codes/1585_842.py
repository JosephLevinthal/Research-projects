x = int(input(" Digite um numero inteiro de quatro digitos: "))
a = x // 1000
b = x // 100 - (a * 10)
c = x // 10 - (a * 100 + b * 10)
d = x - (a * 1000 + b * 100 + c * 10)

print(a + b + c + d)