from numpy import *
from numpy.linalg import *
m_notas=array(eval(input("notas: ")))
linha=shape(m_notas)[0]
zeros=zeros(linha, dtype=float)

for i in range(linha):
	zeros[i]=min(m_notas[i,:])
print(round(sum(zeros)/linha, 2))
