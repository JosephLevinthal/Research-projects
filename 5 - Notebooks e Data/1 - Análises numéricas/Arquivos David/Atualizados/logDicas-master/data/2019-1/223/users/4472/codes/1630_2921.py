jogo1 = float(input("Informe o valor do jogo 1: "))
jogo2 = float(input("Informe o valor do jogo 2: "))

valordesjogo2 = jogo2 - (jogo2 * (25/100))
total = jogo1 + valordesjogo2

print (round(valordesjogo2, 2))
print (round(total, 2))