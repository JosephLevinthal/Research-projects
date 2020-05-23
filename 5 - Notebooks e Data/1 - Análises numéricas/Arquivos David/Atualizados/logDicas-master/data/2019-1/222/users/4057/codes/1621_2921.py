precojogo1 = float(input("Qual o preco do primeiro jogo? "))
precojogo2 = float(input("Qual o preco do sengundo jogo? "))
p1 = precojogo2 - (precojogo2*(25/100))
total = p1 + precojogo1
print(round(p1, 2))
print(round(total, 2))