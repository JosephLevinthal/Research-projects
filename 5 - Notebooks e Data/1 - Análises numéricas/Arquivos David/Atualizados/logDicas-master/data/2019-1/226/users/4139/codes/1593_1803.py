d1=int(input("escreva os quatro digitos:"))

a=int(d1/1000)
x=int(d1/100)
y=int(d1/10)
b=(x%10)
c=(y%10)
d=(d1%10)

r1=(a*5)
r2=(b*4)
r3=(c*3)
r4=(d*2)

s=(r1+r2+r3+r4)%11

print(int(s))
