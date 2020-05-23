#definimos a variavel das gramas por prato
gp=float(input("quantas gramas deu no prato"))
#1kg=1000g
kgp= gp/1000
bebidas=float(input("quantidade de bebidas"))
sobremesas=float(input("quantidade de sobremesa"))
#definimos a variavel dos preços
pb=bebidas*3.50
pp=kgp*26.90
ps=sobremesas*3.00
pt=pb+pp+ps
PT=round(pt,2)
print(PT)
