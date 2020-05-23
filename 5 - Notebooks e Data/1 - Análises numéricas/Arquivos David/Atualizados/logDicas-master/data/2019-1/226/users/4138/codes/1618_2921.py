precojogo1 = float(input("insira o preco do jogo1: "))
precojogo2 = float(input("insira o preco do jogo2: "))

desconto = 25/100

Totaljogo2 = precojogo2 -(precojogo2 * (desconto))

totaljogos = precojogo1 + Totaljogo2

print(round(Totaljogo2,2))
print(round(totaljogos,2))