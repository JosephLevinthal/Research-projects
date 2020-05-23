r1= float(input("insira o valor da resistencia 1: "))
r2= float(input("insira o valor da resistencia 2: "))
r3= float(input("insira o valor da resistencia 3: "))
do= r1*r2*r3   #dominador
de= r1*r2+r2*r3+r1*r3   #denominador
req= do/de
print(req)