from numpy import*
valor_m = int(input("Digite um valor: ")) #se for 2.x deve ser raw_input ao invés de input


resultado = '{0:,}'.format(valor_m).replace(',','.') #Aqui coloca os pontos
print (resultado)