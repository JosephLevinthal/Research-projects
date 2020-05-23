num = int(input("Digite um numero de quatro digitos:\n"))
a = num//1%10
b = num//10%10
c = num//100%10
d = num//1000%10

print((a*2 + b*3 + c*4 + d*5)%11)
