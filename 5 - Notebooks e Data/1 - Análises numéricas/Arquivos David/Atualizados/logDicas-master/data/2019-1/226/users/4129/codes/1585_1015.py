a = int(input('Primeiro:'))
b = int(input('Segundo:'))
c = int(input('Terceiro:'))
maior= max(a, b, c)
menor= min(a, b, c)
meio= (a+b+c-maior-menor)
print(menor, meio, maior)