from numpy import*
v= array(eval(input("Insira seu vetor")))
i=0
e=1/6

vu=size(v)
v1= v**e
v2=vu-1**e

vt= v1+v2/vu**6

print(round(vt,2))