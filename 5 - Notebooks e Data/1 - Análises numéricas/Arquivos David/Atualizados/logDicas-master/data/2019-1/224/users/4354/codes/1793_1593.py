from numpy import * 
notas = array(eval(input("digite os pesos: ")))
pesos = arange(size(notas),dtype = int)
pesos  = pesos + 1
media = (sum(pesos*notas))/(sum(pesos))
print(round(media,2))

