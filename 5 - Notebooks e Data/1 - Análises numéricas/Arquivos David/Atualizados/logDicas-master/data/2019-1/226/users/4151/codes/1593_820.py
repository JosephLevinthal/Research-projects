# Instituto de Computacao - UFAM
# Lab 01 - Ex 10
# 20 / 05 / 2016

valor = int(input("Qual o valor do saque? "))
x=valor//50
r=valor-(x*50)
y=r//10
r2=valor-((y*10)+(x*50))
z=r2//2

print(int(x))
print(int(y))
print(int(z))
