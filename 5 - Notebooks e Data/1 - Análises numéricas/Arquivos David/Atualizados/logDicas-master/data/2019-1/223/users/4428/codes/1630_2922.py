t = float(input("Tempo de investimento: "))

Qf = 1042000
Q0 = 1500

from math import*
i = (((Qf/Q0)**(1/t)) - 1)

print (round(i, 5))