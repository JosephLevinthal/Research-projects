num = int(input("Digite um numero: "))
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10 
d = num % 10
dig = (d*2 + c*3 + b*4 + a*5) % (11)
print(dig)