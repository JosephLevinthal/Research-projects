x=int(input("valor:"))

valor= x%100

nota100=x//100
resto100=nota100%100

nota50=valor//50
resto50=valor%50

resto10=resto50//10

print(int(nota100))
print(int(nota50))
print(int(resto10))
