mg = float(input("escreva a massa do peixe grande: "))
vg = float(input("escreva a velocidade do peixe grande: "))
mp = float(input("escreva a massa do peixe pequeno: "))
vp = float(input("escreva a velocidade do peixe pequeno: "))

v1 = (mg * vg) - (mp * vp)
v2 = mg + mp
vf = v1/v2

print(vf)