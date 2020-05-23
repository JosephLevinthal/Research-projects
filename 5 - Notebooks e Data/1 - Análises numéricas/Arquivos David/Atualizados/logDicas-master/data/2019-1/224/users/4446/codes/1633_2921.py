precojogo1= float(input("valor do primeiro jogo:"))
precojogo2= float(input("valor do segundo jogo:"))
desconto= precojogo2 - 0.25 * precojogo2
total= precojogo1 + desconto

print(round(desconto, 2))
print(round(total, 2))
