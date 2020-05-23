# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identifi
x =int(input("primeiro numero: "))
y =int(input("segundo numero: "))
z =int(input("terceiro numero: "))

minimo =min(x, y, z)
intermediario =(x+y+z-y-x)
maximo =max(x, y, z)
print(minimo,intermediario,maximo)