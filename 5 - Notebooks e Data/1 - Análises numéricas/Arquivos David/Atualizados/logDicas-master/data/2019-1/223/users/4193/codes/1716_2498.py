a=int(input("hab a: "))

b=float(input("hab b: "))

pca=float(input("cidade A: "))

pcb=float(input("cidade B: "))

t=0

while(a<=b):
    a=a+(a*pca/100)
    b=b+(b*pcb/100)
    t=t+1
print(t)