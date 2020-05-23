from numpy import *
a = float(input("Digite: "))
vo = float(input("Digite: "))
n = int(input("Digite: "))
d0 = ((a*0**2)/2) + vo*0
d1 = ((a*1**2)/2) + vo*1
d2 = ((a*2**2)/2) + vo*2
vet = array([d0,d1,d2])
print(vet)