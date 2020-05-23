v1 = int(input("Valor do primeiro resistor: "))
v2 = int(input("Valor do segundo resistor: "))
v3 = int(input("Valor do terceiro resistor: "))

Req = (v1*v2*v3) / ((v1*v2) + (v2*v3) + (v1 * v3))

print(Req)