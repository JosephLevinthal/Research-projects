# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identif// 100icar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
num= int(input("numero inteiro de quatro digitos:"))

q= num // 1% 10
p= num // 10 % 10
r= num // 100% 10
t= num // 1000% 10 

qprt=q+p+r+t
print(qprt)