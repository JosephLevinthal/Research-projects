import math as m
vn= int(input("pontos de vida inicial:"))
D1= int(input("valor do lancamento:"))
D2= int(input("valor do lancamento:"))
d = m.sqrt(5*D1)+(m.pi**(D2/3))

atual= vn - d
print(int(atual+1))

