from math import*
a = float(input())
b = float(input())
c = float(input())
s = (a+b+c)/2
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area,5))
