from numpy import * 
vetor1 = array(eval(input("Digite dados das jogadas de Eusapia:")))
vetor2 = array(eval(input("Digite dados das jogadas de Barsanulfo:")))

cont1 = 0
cont2 = 0
empate = 0
i = 0
tam = size(vetor1)
while size(vetor1-1) > i:
    jogada1 = vetor1[i]
    jogada2 = vetor2[i]
    if vetor1[i] == vetor2[i]:
        empate = empate + 1
    elif jogada1 == 11 and jogada2 == 33:
        cont1 = cont1 + 1
    elif jogada1 == 33  and jogada2 == 22:
        cont1 = cont1 + 1
    elif jogada1 == 22  and jogada2 == 11:
        cont1 = cont1 + 1
    elif jogada2 == 11 and jogada1 == 33:
        cont2 = cont2 + 1
    elif jogada2 == 33  and jogada1 == 22:
        cont2 = cont2 + 1
    else: 
        cont2 = cont2 + 1 
    i= i + 1
    
print(tam)

if cont1 == cont2:
    print("EMPATE")
elif cont1 > cont2:
    print("EUSAPIA")
else:
    print("BARSANULFO")
