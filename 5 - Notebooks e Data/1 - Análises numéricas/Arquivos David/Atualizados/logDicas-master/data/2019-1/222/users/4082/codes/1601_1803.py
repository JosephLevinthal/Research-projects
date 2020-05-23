a = int(input("leia um numero inteiro de quarto digitos:"))
b = a//1000
b1 = a%1000
c = b1//100
c1 = b1%100
d = c1//10
d1 = c1%10
e = d1//1

digito = ((e*2+d*3+c*4+b*5)%11)
print(digito)