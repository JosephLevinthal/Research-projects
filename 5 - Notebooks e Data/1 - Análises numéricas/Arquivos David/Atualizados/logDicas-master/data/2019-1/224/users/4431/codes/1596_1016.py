a=float(input("Digite um lado do triangulo: "))
b=float(input("Digite um lado do triangulo: "))
c=float(input("Digite um lado do triangulo: "))
s=a+b+c
s=s/2
A=s*(s-a)*(s-b)*(s-c)
A=A**0.5
print(round(A,5))
