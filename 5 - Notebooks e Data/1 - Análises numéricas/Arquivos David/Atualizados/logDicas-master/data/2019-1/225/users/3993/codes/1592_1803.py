a=int(input("Insira um numero de 4 digitos:"))
b=a//1000
c=a%1000
d=c//100
e=c%100
f=e//10
g=e%10
h=(g*2+f*3+d*4+b*5)
i=h%11
print(i)