from numpy import *

anderson= float(input("T: "))
vetzones= float(input("O: "))
lindones= int(input  ("P: "))

cont= arange(lindones, dtype=int)
div= zeros(lindones, dtype=float)


demfuncao= (anderson*(cont**2)/ 2 ) + vetzones*cont

print(demfuncao)