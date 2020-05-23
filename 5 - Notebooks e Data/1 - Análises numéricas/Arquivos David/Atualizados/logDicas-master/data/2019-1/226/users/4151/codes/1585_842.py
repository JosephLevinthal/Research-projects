n = int(input("insira um numero de quatro digitos: "))
x1 = n//1000
x2 = (n//100)-(n//1000*10)
x3 = (n//10)-(n//100)*10
x4 = n-(n//10)*10
print(x1+x2+x3+x4)
