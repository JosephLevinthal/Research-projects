from math import*

p=int(input("Insira a vida inicial:"))
D1=int(input("Insira o primeiro valor do dado:"))
D2=int(input("insira o segundo valor do dado:"))


a= (sqrt(5*D1)) + ((pi)**(D2/3))
dano= p-a+1
print(int(dano))