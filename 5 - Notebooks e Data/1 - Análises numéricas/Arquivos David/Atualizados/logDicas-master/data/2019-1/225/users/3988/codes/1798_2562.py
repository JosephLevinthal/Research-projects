from numpy import*

# Leitura do primeiro vetor
vet = array(eval(input("Primeiro vetor: ")))

# Verifica se o programa vai terminar
while (size(vet) > 1):
   # Zera contador de elementos pares
   n = 0

   # Conta quantidade de elementos pares
   for i in vet:
      if (i % 2 == 0):
         n = n + 1 
   # No. de elementos pares
   print(n)

   # No. de elementos impares
   print(size(vet)-n)

   # No. total de elementos
   print(size(vet))

   # Leitura do proximo vetor
   vet = array(eval(input("Proximo vetor: ")))
