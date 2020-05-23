# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
saque = int(input("digite cedula"))
garoupa = saque // 100
espinha = saque % 100
onca = espinha // 50
osso = espinha % 50
bflor = osso // 10
print(int(garoupa))
print(int(onca))
print(int(bflor))
