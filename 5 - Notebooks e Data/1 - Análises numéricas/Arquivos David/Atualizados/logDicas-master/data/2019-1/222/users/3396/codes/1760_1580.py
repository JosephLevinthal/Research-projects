
from numpy import*

v1=array(eval(input("vetor qtd de notas: ")))
v2=array(eval(input("vetor alunos: "))) #mesmo tamanho de v1

i=0
conf=0 #contador de quem faltou
conap=0 #contador de quem aprovou
conre=0 #contador de quem reprovou
comax=0 #contador de quem tirou maior nota

soma = 0
pres = 0

maior = 0
pos = 0
while i < size(v1):         #percorrer o vetor nota
    if v1[i]==(-1):
        conf=conf+1
    
    if v1[i]>=6:
        conap=conap+1
        
    if v1[i]>(-1) and v1[i]<6:
        conre=1+conre
        
    if v1[i] != -1:
        pres = pres+1
        soma = soma + v1[i]
    if v1[i] > maior:
        maior = v1[i]
        pos = i
    i=i+1
            
media=soma/pres
print(conf)
print(conap)
print(conre)        
print(round(media, 2))
print(v2[pos])
