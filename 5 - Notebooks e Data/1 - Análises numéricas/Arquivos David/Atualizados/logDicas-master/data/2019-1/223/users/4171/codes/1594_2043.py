n1 = float(input("nota1:"))
n2 = float(input("nota2:"))
n3 = float(input("nota3:"))
n4 = float(input("nota4:"))

pesonota1 = 1
pesonota2 = 2
pesonota3 = 3
pesonota4 = 4

notatotal = (n1 * pesonota1) + (n2 * pesonota2) + (n3 * pesonota3) + (n4 * pesonota4)
pesodasnotas = (pesonota1 + pesonota2 + pesonota3 + pesonota4)

x = (notatotal/pesodasnotas)

print(round(x,2))