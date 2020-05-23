from numpy import*
itens=array(eval(input("digite o vetor de custo dos itens:")))
total=sum(itens, dtype=float)
print(round(total,2))