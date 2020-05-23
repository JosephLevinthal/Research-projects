R1 = float(input("resistor 1: "))
R2 = float(input("resistor 2: "))
R3 = float(input("resistor 3: "))

req = R1*R2*R3 / (R1*R2 + R2*R3 + R1*R3)


print(req)