from numpy import*
from numpy.linalg import*

ce = array(eval(input("Codigo das filiais: ")))
td = array(eval(input("v:")))
print(ce)
print(td)
z = sum(td)

print("O total de despesas da empresa e:", z, "reais")
