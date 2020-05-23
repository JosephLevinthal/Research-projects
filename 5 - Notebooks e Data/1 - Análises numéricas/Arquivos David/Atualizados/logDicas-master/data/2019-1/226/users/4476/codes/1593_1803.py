a = int(input("digite o numero: "))
b = a//1000
c = a//100 - b*10
d = a//10 - (a//100)*10
e = a - (a//10)*10

n1 = b*5
n2 = c*4
n3 = d*3
n4 = e*2

nt = n1 + n2 + n3 + n4
print(nt % 11)

