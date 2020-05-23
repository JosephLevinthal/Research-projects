valor= int(input("Qual o valor do saque? "))
qtd50=valor // 50
resto_R50 = valor % 50
notas_R10 = resto_R50 // 10
resto_R10 = resto_R50 % 10
notas_R2 = resto_R10 // 2
notas_R50=qtd50
print(int(notas_R50))
print(int(notas_R10))
print(int(notas_R2))