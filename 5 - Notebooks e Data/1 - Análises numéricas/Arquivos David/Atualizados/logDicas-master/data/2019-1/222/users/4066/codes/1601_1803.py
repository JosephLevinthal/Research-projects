conta = int(input("Digite o numero da conta: "))

resto = conta % 10
conta = conta//10
a = resto*2

resto = conta % 10
conta = conta//10
b = resto*3

resto = conta % 10
conta = conta//10
c = resto*4

resto = conta % 10
conta = conta//10
d = resto*5

v = (a+b+c+d)%11

print(v)