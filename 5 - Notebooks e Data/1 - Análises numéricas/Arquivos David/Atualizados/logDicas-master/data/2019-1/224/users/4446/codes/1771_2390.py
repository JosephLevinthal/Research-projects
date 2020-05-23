from numpy import *

vp=array(eval(input("presenca em cada mes: ")))
vf=array(eval(input("faltantes em cada mes: ")))
vetor= vp-vf
d=max(vp)
i=0
while(vp[i]!=d):
	i=i+1
print(i+1)