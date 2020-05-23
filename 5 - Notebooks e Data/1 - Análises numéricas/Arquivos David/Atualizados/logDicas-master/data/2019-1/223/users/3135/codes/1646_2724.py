p=int(input("Insira o primeiro numero:"))
s=int(input("Insira o segundo numero:"))
t=int(input("Insira o terceiro numero:"))

m=min(p,s,t)
M= max(p,s,t)
s=(p+s+t)-m-M

print(s)