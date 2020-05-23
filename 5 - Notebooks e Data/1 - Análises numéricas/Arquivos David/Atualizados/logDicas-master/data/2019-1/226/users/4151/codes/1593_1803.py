n = int(input("insira um numero de quatro digitos: "))
x1 = n//1000
x2 = (n//100)-(n//1000*10)
x3 = (n//10)-(n//100)*10
x4 = n-(n//10)*10
x5= ((x1*5)+(x2*4)+(x3*3)+(x4*2))%11
print(x5)