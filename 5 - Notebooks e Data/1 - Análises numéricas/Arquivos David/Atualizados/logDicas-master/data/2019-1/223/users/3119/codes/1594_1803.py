n = int(input("Digite os numeros: "))

a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10

m = (a*5)+(b*4)+(c*3)+(d*2)

soma = m % 11

print(soma)