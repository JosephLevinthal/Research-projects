#primeiramente definimos as variaveis
a=float(input("numero a"))
b=float(input("numero b"))
c=float(input("numero c"))
#definmos a variavel da formula matematica
chernobyl=((a**2)+(b**2)+(c**2))/(a+b+c)
real=round(chernobyl, 7)
#imprimimos o resultado
print(real)
