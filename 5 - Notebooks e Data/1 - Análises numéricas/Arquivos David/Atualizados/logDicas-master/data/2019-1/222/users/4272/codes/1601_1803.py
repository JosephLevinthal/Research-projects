num = int(input("quatro digito:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

soma = (u*2 + d*3 + c*4 + m*5) % 11
print(soma)
