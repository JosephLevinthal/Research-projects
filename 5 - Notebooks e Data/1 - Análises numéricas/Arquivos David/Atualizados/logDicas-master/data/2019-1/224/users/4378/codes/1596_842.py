entrada = int(input("numero de quatro digitos"))
pri_dig = entrada // 1000
pergarsegdigito = entrada % 1000
seg_dig = pergarsegdigito // 100
pergarterceirodigito = pergarsegdigito % 100
ter_dig = pergarterceirodigito // 10
pegarquartodigito = pergarterceirodigito % 10
quar_dig = pergarterceirodigito % 10

soma_dos_digitos = pri_dig + seg_dig + ter_dig + quar_dig
print(soma_dos_digitos)
