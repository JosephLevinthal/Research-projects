from numpy import* 
vet = array(eval(input("N inteiros:")))

y = array( [x for x in vet if x>0])
print(y)