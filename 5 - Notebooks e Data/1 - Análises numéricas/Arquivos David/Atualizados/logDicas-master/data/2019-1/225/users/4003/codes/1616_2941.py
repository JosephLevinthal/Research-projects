vi = float(input("valor incial:"))
j = float(input("juros:"))
n = float(input("meses:"))
vf = vi * (1+j) ** n
print(round(vf,2))