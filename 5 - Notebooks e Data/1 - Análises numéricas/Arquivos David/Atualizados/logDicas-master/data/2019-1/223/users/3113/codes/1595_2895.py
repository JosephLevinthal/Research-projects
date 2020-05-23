# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
quantidade  = int(input("Qual o valor unitario do jogo? "))
valor  = float(input("Qual o valor unitario do jogo? "))
frete  = float(input("Qual o valor unitario do jogo? "))

# Calculo do valor a ser pago, incluindo o frete:
total = valor*quantidade+frete

# Impressao do valor total:
print(total)