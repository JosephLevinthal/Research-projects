a = int(input("numero: "))
b = int(input("numero: "))
c = int(input("mumero: "))  

menor = min(a,b,c)
maior = max(a,b,c)
medio = a+b+c-maior-menor
print(menor,medio,maior)