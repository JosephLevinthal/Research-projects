a = int(input("digite um numero com quatro digitos: "))
b= a // 1000
b1 = a % 1000
c = b1 // 100
c1 = b1 % 100
d = c1 // 10
d1 = c1 % 10
e = d1 // 1
total = (b+c+d+e)
print(total)