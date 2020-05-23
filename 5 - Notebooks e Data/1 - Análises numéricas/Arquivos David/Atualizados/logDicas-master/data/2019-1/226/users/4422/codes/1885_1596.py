from numpy import*
v = array(eval(input('notas: ')))
med = (sum(v) - min(v))/(size(v) - 1)
print(round(med, 2))