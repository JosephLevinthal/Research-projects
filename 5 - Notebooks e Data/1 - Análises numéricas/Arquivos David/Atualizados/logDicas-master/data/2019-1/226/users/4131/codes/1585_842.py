# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
vr=int(input("quatro digitos:"))
n1=vr//1000
n2=vr//100-(vr//1000)*10
n3=vr//10- (vr//100)*10
n4=vr//1- (vr//10)*10
print(n1+n2+n3+n4)