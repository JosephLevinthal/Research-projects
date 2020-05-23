la=float(input("comprimento a: "))
lb=float(input("comprimento b; "))
lc=float(input("comprimento c: "))
semip=(la+lb+lc)/2
from math import *
at=sqrt(semip*(semip-la)*(semip-lb)*(semip-lc))
print(round(at, 5))

