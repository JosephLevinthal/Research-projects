from numpy import*
vnotas=array(eval(input("Digite as notas:")))
menornota=min(vnotas)
medaluno=(sum(vnotas)-menornota)/(size(vnotas)-1)
print(round(medaluno,2))