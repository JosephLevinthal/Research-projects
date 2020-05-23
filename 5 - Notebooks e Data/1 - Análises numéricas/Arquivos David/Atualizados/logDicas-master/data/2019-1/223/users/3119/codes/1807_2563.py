from numpy import*

# Leitura do primeiro vetor
vet = array(eval(input("Primeiro vetor: ")))

while (size(vet) > 1):
   a = 0
	
   for elemento in vet:
      if (elemento >= 5 and elemento < 7):
         a = a + 1
			
   print(a)

   vet = array(eval(input("Proximo vetor: ")))
