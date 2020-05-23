from numpy import*

# Leitura do primeiro vetor
vet = array(eval(input("Primeiro vetor: ")))
nimpar = 0
h = 1
# Verifica se o programa vai terminar
while (size(vet) > h):
   # Zera contador de elementos pares
   npar = 0

   # Conta quantidade de elementos pares
   for elemento in vet:
      if (elemento % 2 == 0):
         npar = npar + 1
      else:
         nimpar += 1
   h += 1 
   # No. de elementos pares
   print(npar)

   # No. de elementos impares
   print(nimpar)

   # No. total de elementos
   print(size(vet))

   # Leitura do proximo vetor
   vet = array(eval(input("Proximo vetor: ")))
   npar = 0
   nimpar = 0
   h = 1
