# Entrada das notas dos alunos:
N1 = float(input("Entrada da nota 1: "))
N2 = float(input("Entrada da nota 2: "))
N3 = float(input("Entrada da nota 3: "))
N4 = float(input("Entrada da nota 4: "))

# Calculo da media ponderada:
MP = (N1*1 + N2*2 + N3*3 + N4*4)/10
print(round(MP, 2))