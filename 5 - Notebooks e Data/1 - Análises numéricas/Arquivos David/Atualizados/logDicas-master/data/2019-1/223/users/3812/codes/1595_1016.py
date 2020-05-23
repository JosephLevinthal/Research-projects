x = float(input('digite o valor de x: '))
y = float(input('digite o valor de y: '))
z = float(input('digite o valor de z: '))

s = (x+y+z)/2

A = (s*(s-x)*(s-y)*(s-z))**(1/2)

print(round(A,5))