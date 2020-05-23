from numpy import* #importa a biblioteca que trabalha com vetores

# Leitura do primeiro vetor
vet = array(eval(input("Primeiro vetor: "))) #vetor numerico

# Verifica se o programa vai terminar
while (size(vet) > 1): #A funcao while eh necessaria para se repetir a pergunta indefinidamente
   # Zera contador de elementos pares
   npar = 0

   # Conta quantidade de elementos pares
   for elemento in vet: #le diretamento o elemento, e nao o indice
      if (elemento % 2 == 0): #verifica se o elemento eh par
         npar = npar + 1 #se Verdade, contador par eh incrementado em 1

   # No. de elementos pares
   print(npar)

   # No. de elementos impares
   print(size(vet) - npar)

   # No. total de elementos
   print(size(vet))

   # Leitura do proximo vetor
   vet = array(eval(input("Proximo vetor: ")))
