from numpy import*
v=array(eval(input(":")))
soma=sum(v)
m=(((soma+1)**6)/size(v))**(1/9)
print(round(m,2))