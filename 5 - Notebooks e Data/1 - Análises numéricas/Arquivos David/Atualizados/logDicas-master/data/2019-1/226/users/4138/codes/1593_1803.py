C = int(input("digite sua conta bancaria:"))
C1 = C//1000
Ci = C1 * 5
C2 = C//100 - (C1*10)
Cii = C2 * 4
C3 = C//10 - (C//100) * 10
Ciii = C3 * 3
C4 = C % 10
Civ = C4 * 2
Ct = (Ci + Cii + Ciii + Civ)
DV = Ct % 11
print(DV)