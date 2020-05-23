from numpy import*
vet = array(eval(input("Primeiro vetor: ")))
while (size(vet) > 1):
   npar = 0
   for n in vet:
      if (n>=5 and n<7):
         npar = npar + 1
		print(npar)



	