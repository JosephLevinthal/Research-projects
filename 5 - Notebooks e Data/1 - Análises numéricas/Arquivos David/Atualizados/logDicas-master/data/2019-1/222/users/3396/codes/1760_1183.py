from numpy import * 

vetor = array(eval(input("Digite numeros inteiros:")))

tam_v = size(vetor)
i = 0
cont = 0
while tam_v > i: 
    if vetor[i] > 0:
        cont = cont +1
        i = i+1
    else: 
        i = i +1
vetor2 = arange((cont))
j = 0
i = 0
tam = size(vetor2) 
while tam > i: 
    if vetor[j] > 0:
        con = vetor[j]
        vetor2[i] = con
        i = i+1
        j = j+1
    else: 
        j = j +1
print(vetor2)
