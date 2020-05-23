valor=float(input("Qual o valor do saque "))
notas_R50 = valor // 50
resto_R50= valor % 50
resto_R10 = resto_R50 % 10
notas_R2 = resto_R10 // 2
notas_R10 = resto_R50 // 10
print(int(notas_R50))
print(int(notas_R10))
print(int(notas_R2))