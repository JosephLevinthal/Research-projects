# quantidade de notas de 100 
a = int(input("Valor do saque:"))

# Quantidade de notas de 100
b = int(a // 100)
#Resto 
c = (a % 100)

#Quantidade de notas de 50
d = c // 50

# resto 
e =  c % 50

# quantidade de nota de 10
f = e//10

print(int(b))
print(int(d))
print(int(f))