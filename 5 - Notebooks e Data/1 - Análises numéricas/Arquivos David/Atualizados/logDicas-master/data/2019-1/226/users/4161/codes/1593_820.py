valor = int(input("Qual o valor do saque? "))
notas_Rs50 = valor // 50
resto_Rs50 = valor % 50
notas_Rs10 = resto_Rs50 // 10
resto_Rs10 = resto_Rs50 % 10
notas_Rs2 = resto_Rs10 // 2
print(int(notas_Rs50))
print(int(notas_Rs10))
print(int(notas_Rs2))
