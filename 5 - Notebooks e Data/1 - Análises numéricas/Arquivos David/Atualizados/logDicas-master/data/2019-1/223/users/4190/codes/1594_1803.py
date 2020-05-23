num=int(input("Digite um numero de quatro digitos: "))
a= num//1%10
b= num//10%10
c= num//100%10
d= num//1000%10
soma=a*2+b*3+c*4+d*5
total=soma%11
print(total)