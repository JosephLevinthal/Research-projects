x = int(input("quatro digitos:"))
a = x // 1000#
b = x%1000
c = b//100#
d = b%100
e = d // 10#
f = d%10#
r = a * 2
s = c*3
t = e * 4
u = f*5
g = (r+s+t+u)%11
print( g )