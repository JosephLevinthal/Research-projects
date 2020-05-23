from numpy import *

ent = input("ent:")
num = len(ent)
print(ent.replace(" ","").upper())
n = ent[0]
inv = ent[-1]
if (n==inv):
   print(1)
else:
   print(0)
