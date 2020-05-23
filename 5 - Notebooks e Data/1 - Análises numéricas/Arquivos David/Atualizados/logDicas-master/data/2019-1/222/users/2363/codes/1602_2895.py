# Este código é apenas um ESBOÇO da solução.
# Modifique-o para atender as especificações do enunciado.

# Leitura das entradas e conversao para float:
Qty=int(input("Numero de Jogos  "))
Valor_Jogo = float(input("Qual o valor unitario do jogo?  "))
Frete= float(input("O valor do frete e "))

# Calculo do valor a ser pago, incluindo o frete:
Total = (Qty*Valor_Jogo) + Frete

# Impressao do valor total:
print(Total)