
F=273.1
R=0.082057
t=float(input("temperatura:"))
p=float(input("presao:"))
v = float(input("volume:"))
n = float(input("mols:"))
T = ((p*v)//n*R)-F
V = (n*R*(t+F))//p
N = ((p*v))//R*(t+F)
print(N)
print(V)
print(T)
