p = float(input ("pressao? "))
n = float(input("mols? "))
t = float(input("temperatura? "))
t+= 273.15
R = 0.082
print((n*R*t)/p)