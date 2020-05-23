x = int(input("digitos: "))

l = x % 10
h = (x // 10) % 10
g = (x // 100) % 10
k = (x // 1000) % 10

soma = (l*2) + (h*3) + (g*4)+ (k*5)
dg = soma % 11

print(dg)