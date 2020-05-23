import math
n=int(input())
prob=1-((math.factorial(365))/math.factorial(365-n))*(1/(365**n))
print(round(100*prob,2))