num = int(input("senha de quatro digitos: "))
d1 = num//1000
d2 = num//100 - (d1*10)
d3 = num//10 -(num//100)*10
d4 = num%10 

verificacao = (5*d1 + 4*d2 + 3*d3 + 2*d4)%11
print(verificacao)
