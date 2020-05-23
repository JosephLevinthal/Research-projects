from math import *

qo = float(input("Digite o valor inicial: ")) 
qf = float(input("Digite o valor final: "))
y  = int(input("Digite a quantidade de anos: "))

r = (log(qf)-log(qo))/y

print(r)