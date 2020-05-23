import math

HP=float(input())
D1=int(input())
D2=int(input())
dano=int(math.sqrt(5*D1)+math.pi**(D2/3))
HP=HP-dano
print(HP)