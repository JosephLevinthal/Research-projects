
p=float(input("pressao"))
n=float(input("numero de mols"))
t=float(input("temperatura"))
r= 0.082
s= 273.15+t
v=n * r * s / p
print(v)
