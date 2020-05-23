# Leitura dos numeros a partir do teclado e conversao para int:
n1 = int(input("digite um numero: "))
n2 = int(input("digite um segundo numero: "))
n3 = int(input("digite um terceiro numero: "))

# ordenacao nos numeros em ordem crescente:
print(min(n1, n2, n3))
print((n1+n2+n3)-(min(n1, n2, n3)+max(n1, n2, n3)))
print(max(n1, n2, n3))

