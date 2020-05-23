# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
entrada = int(input("numero de quatro digitos:"))
primeiro_digito = entrada //1000
pegarsegdigito = entrada % 1000
seg_dig = pegarsegdigito // 100
pegarterceirodigito = pegarsegdigito % 100
ter_dig = pegarterceirodigito //10
pegarquartodigito = pegarterceirodigito % 10
quar_dig = pegarterceirodigito % 10
soma_dos_digitos = primeiro_digito + seg_dig + ter_dig + quar_dig
print(soma_dos_digitos)