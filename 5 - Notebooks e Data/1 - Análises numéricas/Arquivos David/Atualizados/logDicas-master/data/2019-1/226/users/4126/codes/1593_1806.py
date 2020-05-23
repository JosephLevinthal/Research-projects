from math import*
pr = float(input(" npc "))
pn = 1 - (factorial(365)/factorial(365 - pr)) * (1/(365**pr))
pro = pn * 100
print(round(pro,2))