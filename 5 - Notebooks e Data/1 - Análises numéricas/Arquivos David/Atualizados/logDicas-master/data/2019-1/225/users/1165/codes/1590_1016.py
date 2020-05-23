a = float(input("insira um valor de a: "))
b = float(input("insira um valor de b: "))
c = float(input("insira um valor de c: "))

from math import*
semi = (a+b+c)/2
area = semi*(semi-a)*(semi-b)*(semi-c)
y = sqrt(area)
print(round(y, 5))

