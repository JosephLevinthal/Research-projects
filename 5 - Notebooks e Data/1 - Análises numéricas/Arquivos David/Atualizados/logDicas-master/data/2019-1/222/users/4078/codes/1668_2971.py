taxa_de_juros = float(input"taxa de juros: ")
valor_do_apatamento = float(input("valor do ap: "))

valor_inicial = 1500
tempo = 36

qt = 1500*(1 + taxa_de_juros)**tempo

print(qt)