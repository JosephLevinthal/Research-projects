ML = float(input("media dos laboratorios: "))
MT = float(input("media dos trabalhos: "))
MP = float(input("media das provas: "))
NF = float((25*ML + 30*MT + 45*MP) / 100)
print(round(NF, 2))