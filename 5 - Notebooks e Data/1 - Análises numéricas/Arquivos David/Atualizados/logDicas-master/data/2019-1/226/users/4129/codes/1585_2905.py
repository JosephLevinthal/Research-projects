from math import*
#Lados do triangulo
a = float(input('Lado a:'))
b = float(input('Lado b:'))
c = float(input('Lado c:'))
#semiperimetro
s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area, 5))