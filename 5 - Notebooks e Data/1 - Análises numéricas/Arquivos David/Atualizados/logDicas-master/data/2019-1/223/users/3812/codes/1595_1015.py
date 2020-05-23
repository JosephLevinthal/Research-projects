x = int(input('digite o valor de x: '))
y = int(input('digite o valor de y: '))
z = int(input('digite o valor de z: '))

a = min(x, y, z)
b = max(x, y, z)
c = x + y + z - a - b

print(a)
print(c)
print(b)