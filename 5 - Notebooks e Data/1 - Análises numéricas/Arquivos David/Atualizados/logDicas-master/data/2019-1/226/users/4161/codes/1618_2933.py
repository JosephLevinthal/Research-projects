from math import*
q0 = float(input("valor inicial investido: "))
qf = float(input("valor final pretendido: "))
y = float(input("duracao em anos do investimento: "))
r = (log(qf) - log(q0))/y
print(r)