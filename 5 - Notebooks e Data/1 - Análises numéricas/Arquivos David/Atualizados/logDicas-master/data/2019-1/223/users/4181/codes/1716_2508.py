n = int(input())
formula = 3
cont = 2
denominador = 0
i = 2
if(n==1):
    print(round(formula,8))
else:
    while (1):
        if(i==n+1):
            break
        if(i % 2 !=0 and i>1):
            denominador = (cont * (cont+1) *(cont+2))
            formula -= 4/denominador
            #print(denominador)
        else:
            denominador = cont * (cont+1) *(cont+2)
            formula += 4/denominador
        cont += 2
        i = i+1
    print(round(formula,8))