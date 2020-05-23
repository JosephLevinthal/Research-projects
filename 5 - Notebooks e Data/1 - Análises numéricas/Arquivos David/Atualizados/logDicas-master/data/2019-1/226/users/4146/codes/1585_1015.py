# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
na = int(input("numero a "))
nb = int(input("numero b "))
nc = int(input("numero c "))
vlmax = max(na, nb, nc)
vlmin = min(na, nb, nc)
vlint = (na+nb+nc) - (vlmax+vlmin)
print(vlmin)
print(vlint)
print(vlmax)
