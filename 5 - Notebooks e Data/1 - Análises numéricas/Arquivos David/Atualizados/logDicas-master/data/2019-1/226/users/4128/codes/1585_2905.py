from math import*  sqrt

a = float(input("farofa de banana"))
b = float(input("farofa de jaba"))
c = float(input("farofa de ovo"))
s = (a+ b+ c)/2
a1 = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(a1, 5))
#sqrt = raiz quadrada
#al = area de um triangulo
