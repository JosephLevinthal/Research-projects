valor = int(input("valor a ser sacado: "))

notasde100 = (valor//100)

restode100 = (valor % 100)

notasde50 = (restode100 // 50)

restode50 = (restode100 % 50)

notasde10 = (restode50 // 10)

print(notasde100)
print(notasde50)
print(notasde10)