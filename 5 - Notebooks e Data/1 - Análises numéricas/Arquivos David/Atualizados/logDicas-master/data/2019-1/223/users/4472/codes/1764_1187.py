# Nome: Nathaly Barbosa Leite
# Curso: Estatística
# Matrícula: 21954721

from numpy import *

palavra = str(input("Informe uma palavra: "))

#Primeiro caractere da string;
print (palavra[0])

#Último caractere da string;
print (palavra[-1])

#Quantidade de caracteres da string;
print (len(palavra))

#Toda a string em caracteres minúsculos;
print (palavra.lower())

#Toda a string em caracteres maiúsculos;
print (palavra.upper())

#Impressão de 500 cópias da string
imprimir = palavra * 500
print(imprimir)