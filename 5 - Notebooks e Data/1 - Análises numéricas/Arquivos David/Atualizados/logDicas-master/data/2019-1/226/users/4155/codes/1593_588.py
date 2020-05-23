v = int(input("valor do saque: "))

notas100 = v // 100 
resto100 = v % 100
notas50 = resto100 // 50
resto50 = resto100 % 50
nota10 = resto50 // 10

print(notas100)
print(notas50)
print(nota10)