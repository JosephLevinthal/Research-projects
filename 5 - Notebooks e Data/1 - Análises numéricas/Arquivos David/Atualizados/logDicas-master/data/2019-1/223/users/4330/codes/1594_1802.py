from math import*

p=int(input("Insira a vida inicial:"))
D1=int(input("Insira o primeiro valor do dado:"))
D2=int(input("Insira o segundo valor dado:"))


a=(sqrt(5*D1)) + ((pi)**(D2/3))
dano=p-a+1
print(int(dano))
