numeroloco = int(input("senha de quatro digitos: "))

x1 = numeroloco//1000
x2 = numeroloco//100 - (numeroloco//1000)*10
x3 = numeroloco//10  - (numeroloco//100)*10
x4 = numeroloco//1   - (numeroloco//10)*10

x =  ((x1*5) + (x2*4) + (x3*3) + (x4*2))% 11
print(x)