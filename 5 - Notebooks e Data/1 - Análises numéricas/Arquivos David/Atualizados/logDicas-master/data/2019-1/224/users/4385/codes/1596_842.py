entrada = int(input("numero de quatro digitos"))
pri_dig = entrada // 1000
pegarsegdigito = entrada % 1000
seg_dig = pegarsegdigito // 100
pegarterceirodigito = pegarsegdigito % 100
ter_dig = pegarterceirodigito // 10
pegarquartodigito = pegarterceirodigito % 10
quar_dig = pegarterceirodigito % 10

soma_dos_digitos = pri_dig + seg_dig + ter_dig + quar_dig
print(soma_dos_digitos)