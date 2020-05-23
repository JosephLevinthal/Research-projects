from numpy import*
vet = array(eval(input("Primeiro vetor: ")))
h=0
while (size(vet) > 1):
   npar = 0  
   for elemento in vet:
      if (elemento % 2 == 0):
         npar = npar + 1 
   print(npar)
   print(size(vet)-npar)
   print(size(vet))
   vet = array(eval(input("Proximo vetor: ")))
