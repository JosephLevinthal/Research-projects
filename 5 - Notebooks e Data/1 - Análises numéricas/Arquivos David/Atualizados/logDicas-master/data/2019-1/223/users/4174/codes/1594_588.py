# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.

saldo = int(input("qual o valor:"))
n1 = int(input("qual a cedula:"))
n2 = int(input( "qual a cedula:"))
n3 = int(input("qual a cedula:"))

cdl1 = (n1%80)
cdl2 = (n2%20)
cdl3 = (n3%10)

verba = (cdl1 - cdl2 - cdl3)
print(verba)