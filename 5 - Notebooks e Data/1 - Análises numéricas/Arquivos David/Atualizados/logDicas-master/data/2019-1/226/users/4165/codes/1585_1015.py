var1 = int(input(" numero 1 "))
var2 = int(input(" numero 2 "))
var3 = int(input(" numero 3 "))
menor = min(var1 ,var2 ,var3)
maior = max(var1 ,var2 ,var3)
meio = (var1 + var2 + var3) - menor - maior
print(menor)
print(meio)
print(maior)