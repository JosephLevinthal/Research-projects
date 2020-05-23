j = float(input("digite uma taxa: "))
Qo = 1500
t = 36

Qf = Qo * (1 + j) ** t

print(round(Qf, 2))