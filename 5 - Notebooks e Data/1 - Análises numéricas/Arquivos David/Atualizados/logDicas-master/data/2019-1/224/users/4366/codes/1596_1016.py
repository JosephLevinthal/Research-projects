from math import*
a=float(input("Digite a:"))
b=float(input("Digite b:"))
c=float(input("Digite c:"))
s=(a+b+c)/2
Area=sqrt(s*(s-a)*(s-b)*(s-c))
print(round(Area,5))