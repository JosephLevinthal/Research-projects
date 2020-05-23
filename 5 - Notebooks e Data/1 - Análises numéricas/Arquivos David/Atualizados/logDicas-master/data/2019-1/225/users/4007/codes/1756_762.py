vet_mes = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
d = input("data(dd/mm/aaaa) ")
dia = int(d[:2])
m = int(d[2:4])
ano = d[-4:]
me = vet_mes[m-1]		0
print(dia, "de", me, "de", ano)
