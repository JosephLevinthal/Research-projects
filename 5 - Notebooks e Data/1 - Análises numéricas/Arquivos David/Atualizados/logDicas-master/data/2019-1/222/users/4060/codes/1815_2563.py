from numpy import*

# Leitura do primeiro vetor
media = array(eval(input("informe as medias: ")))

# Verifica se o programa vai terminar
while (size(media) > 1):
   # Zera contador de elementos pares
   n_tem_condicoes = 0

   # Conta quantidade de elementos pares
   for elemento in media:
      if (elemento>=5)and(elemento<7):
         n_tem_condicoes = n_tem_condicoes + 1

   # No. de elementos sem condicoes
   print(n_tem_condicoes)
	
	# Leitura do proximo vetor
   media = array(eval(input("informe as medias: ")))
