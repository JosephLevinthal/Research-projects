qtd = int(input("Digite a quantidade de jogos: "))
valor = float(input("Digite o valor qu unitario dos jogos: "))
frete= float(input("Digite o valor do frete: "))

preco_total= frete + ( qtd * valor )

print(preco_total)