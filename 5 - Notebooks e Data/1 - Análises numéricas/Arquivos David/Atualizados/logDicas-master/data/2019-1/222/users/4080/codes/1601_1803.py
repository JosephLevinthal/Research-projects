a = int(input("digite o numero: "))
b = a//1000
b1 = a%1000
c = b1//100
c1 = b1%100
d = c1//10
d1 = c1%10
e = d1//1
x = (b*5+c*4+d*3+e*2)
y = (x%11)
print(y)