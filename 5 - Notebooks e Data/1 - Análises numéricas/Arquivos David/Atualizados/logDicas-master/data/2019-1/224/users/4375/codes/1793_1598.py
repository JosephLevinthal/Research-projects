from numpy import*
itens=array(eval(input("custo dos itens: ")))
total=sum(itens,dtype=float)
print(round(total,2))