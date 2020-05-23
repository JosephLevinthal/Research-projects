import math 
a= float(input("Digite o comprimento a do triangulo: "))
b= float(input("Digite o comprimento b do triangulo: "))
c= float(input("Digite o comprimento c do triangulo: "))
s= ((a + b + c)/2)
A= (s*(s - a)*(s - b)*(s - c))
B= math.sqrt(A)
print(round(B, 5))
