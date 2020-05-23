n =float(input("numero inteiro de quatro digitos: "))

a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

soma = a + b + c + d
print(soma)