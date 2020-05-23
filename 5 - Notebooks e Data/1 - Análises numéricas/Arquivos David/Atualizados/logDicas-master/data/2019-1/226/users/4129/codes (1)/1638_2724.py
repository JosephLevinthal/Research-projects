x1 = int(input("Primeiro numero:"))
x2 = int(input("Segundo numero:"))
x3 = int(input("Terceiro numero:"))

maior = max(x1,x2,x3)
menor = min(x1,x2,x3)
meio = x1+x2+x3 - maior - menor
print(meio)