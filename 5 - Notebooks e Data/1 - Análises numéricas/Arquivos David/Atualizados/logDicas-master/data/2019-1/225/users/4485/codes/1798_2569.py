from numpy import*
vet = array(eval(input("")))
media = vet.sum()/len(vet)
vet = (vet - media)
vet = vet**2
r = (vet.sum()/(len(vet)-1))**(1/2)
print(round(r,3))