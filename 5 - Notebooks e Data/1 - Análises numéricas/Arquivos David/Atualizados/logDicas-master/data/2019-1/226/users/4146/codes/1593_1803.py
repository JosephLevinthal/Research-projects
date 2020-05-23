a = int(input("Numero: "))
mil = a//1000
cem = a//100 - (mil*10)
dez = a//10 - (a//100)*10
uni = a%10

verificacao = (5*mil + 4*cem + 3*dez + 2*uni)%11
print(verificacao)
