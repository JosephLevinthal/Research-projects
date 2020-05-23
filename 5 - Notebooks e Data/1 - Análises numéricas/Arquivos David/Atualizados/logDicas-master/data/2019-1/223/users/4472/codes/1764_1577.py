# Nome: Nathaly Barbosa Leite
# Curso: Estatística
# Matrícula: 21954721

from numpy import *

aceleracao = float(input("Aceleracao do carro: "))
velocidadeInicial = float(input("Velocidade Inicial: "))
N = int(input("Quantidade de Posicoes: "))

t = arange(N)
d = zeros(N,dtype=int)
 
vetorResultado = array(((aceleracao * (t ** 2) / 2)) + (velocidadeInicial * t))

print(vetorResultado)

