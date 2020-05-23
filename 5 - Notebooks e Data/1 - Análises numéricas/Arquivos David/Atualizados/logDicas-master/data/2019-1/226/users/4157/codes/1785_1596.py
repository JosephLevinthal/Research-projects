from numpy import*
vet = array(eval(input("notas do estudante:")))
me = (sum(vet)-min(vet))/(size(vet)-1)
print(round(me, 2))
