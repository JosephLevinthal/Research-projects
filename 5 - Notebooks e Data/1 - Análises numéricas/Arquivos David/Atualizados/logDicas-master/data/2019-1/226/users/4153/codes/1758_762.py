from numpy import *
# Vetor contendo o nome dos meses do ano
vm = array(["janeiro", "fevereiro","marco","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"])
v = input("Insira o mes: ")

dd = v[:2]
mm = v[2:4]
aa = v[4:]
mm = int(mm)-1
msg = dd+ " de "+ vm[mm]+" de "+aa
print(msg)