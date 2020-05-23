valor=int(input("qual valor deseja sacar: "))
notas_100= valor//100
rest_100= valor%100
notas_50= rest_100//50
rest_50= rest_100%50
notas_10=rest_50//10

print(notas_100)
print(notas_50)
print(notas_10)
