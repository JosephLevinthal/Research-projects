# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
dia = int(input("Valor do dia:"))
diafut = int(input("Numero de dias:"))

futuro = (dia+diafut) % 7

if( dia>= 0) and (dia <= 6):
