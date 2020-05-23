import math
a= float(input("quanto vale a: "))
b= float(input("quanto vale b: "))
c= float(input("quanto vale c: "))
s= (a+b+c)/2
Z= math.sqrt(s*(s-a)*(s-b)*(s-c))
print(round(Z, 5))
