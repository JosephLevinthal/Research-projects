from numpy import *

v = array(eval(input("Digite notas:")))*1.0
n = array(eval(input("Digite nome alunos: ")))

i =0
faltas=0
aprovados=0
reprovados=0
soma=0
while(i<size(v)):
   if(v[i]==-1.0):
    	faltas +=1
   if(v[i]>=6):
      aprovados+=1
      soma+=v[i]
   if(v[i]<6.0 and v[i]!=-1.0):
      reprovados+=1
      soma+=v[i]
   if(v[i]==max(v)):
      nome = n[i]
   i=i+1
print(faltas)
print(aprovados)
print(reprovados)
print(round(soma/(aprovados+reprovados),2))
print(nome)