a = float(input("digite um valor para a:"))
b = float(input("digite um valor para b:"))
c = float(input("digite um valor para c:"))
s = a/2+b/2+c/2
from math import*
area = sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area, 5))
