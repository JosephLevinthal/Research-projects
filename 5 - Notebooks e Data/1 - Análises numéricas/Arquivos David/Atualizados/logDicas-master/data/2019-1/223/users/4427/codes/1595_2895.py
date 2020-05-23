# Leitura da entrada de quantidade de jogos
jogos = int(input("Quantidade de jogos: "))

# Leitura das entradas e conversao para int e float:
var = float(input("Qual o valor unitario do jogo? "))
frete = float(input("Qual o valor do frete?"))

# Calculo do valor a ser pago, incluindo o frete:
total = (var*jogos+frete)

# Impressao do valor total:
print(total)