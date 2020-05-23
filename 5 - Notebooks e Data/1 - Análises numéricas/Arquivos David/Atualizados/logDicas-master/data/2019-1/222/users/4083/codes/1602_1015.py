# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
var1 = int(input("a")) 
var2 = int(input("b")) 
var3 = int(input("c")) 
menor = min(var1,var2,var3)
maior = max(var1,var2,var3)
meio = (var1 + var2 + var3) - (maior + menor) 
print(menor)
print(meio)
print(maior)