from numpy import*
c = array(eval(input("Vetor de custos: ")))
ct = sum(c) - (sum(c)/15)*100
print(round(ct,2))
print(sum(c))