from numpy import *

pro = array(eval(input("gols pro :")))
contra = array(eval(input("gols contra:")))
vc = zeros(3,dtype=int)
for i in range(0,size(pro)):
    if(pro[i]>contra[i]):
      vc[0]=vc[0]+1
    if(pro[i]==contra[i]):
      vc[1]=vc[1]+1
    if(pro[i]<contra[i]):
      vc[2]=vc[2]+1
print(vc)