# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
dig = int(input("Digite quatro numeros:"))
dig%10
d1= dig//10
dd = d1%10
d2= dig//100
dd1 = d2%10
d3 = dig//1000
dd2 = d3%10
soma = dig%10 + dd + dd1 + dd2 
print(soma)