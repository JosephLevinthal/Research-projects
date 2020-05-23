n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
p1 = 1
p2 = 2
p3 = 3
p4 = 4

peso = p1 + p2 + p3 + p4
nota = (n1 * p1) + (n2 * p2) + (n3 * p3) + (n4 * p4) 

media = nota / peso

print (round(media, 2))