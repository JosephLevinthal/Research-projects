var = int(input())

milhar = var//1000
centena = (var%1000)//100
dezena = (var%100)//10
unidade = (var%1000)%10

r = ( (milhar * 5) + (centena * 4) + (dezena * 3) + (unidade * 2) )%11

print(r)
