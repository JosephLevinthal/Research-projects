from numpy import*
from numpy.linalg import*
n=array(eval(input("insira as horas de trabalho de cada funcionario: ")))
t=shape(n)[1]
mt=zeros(t,dtype=int)
for i in range(t):
	mt[i] = sum(n[:,i])
a=(mt[0])
b=(mt[1])
c=(mt[2])
d=(mt[3])
e=(mt[4])
f=(mt[5])
g=(mt[6])
v=max(mt)
if a==v:
	print("1")
if b==v:
	print("2")
if c==v:
	print("3")
if d==v:
	print("4")
if e==v:
	print("5")
if f==v:
	print("6")
if g==v:
	print("7")