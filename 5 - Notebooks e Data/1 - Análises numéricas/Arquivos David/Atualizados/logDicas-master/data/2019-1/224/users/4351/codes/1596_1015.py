#definimos a variavel dos numeros inteiros
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
#definimos a variavel do minimo
minimo=min(a,b,c)
#definimos a variavel do maximo
maximo=max(a,b,c)
#definimos a variavel do intermediario
inter=(a+b+c)-minimo-maximo
#imprimimos tudo
print(minimo)
print(inter)
print(maximo)
