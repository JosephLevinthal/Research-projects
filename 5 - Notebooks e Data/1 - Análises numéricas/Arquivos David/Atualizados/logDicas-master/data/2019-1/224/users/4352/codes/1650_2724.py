a = int(input("digite um numero: "))
b = int(input("digite outro: "))
c = int(input("digita mais um: "))
maior = max(a, b, c)
menor = min(a, b, c)
soma = a + b + c
sub = soma - maior - menor
print(sub)