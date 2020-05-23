from numpy import*
vet = array(eval(input("Media: ")))


while (size(vet) > 1):
   m = 0
   total = 0
   for elemento in vet :
      if (elemento >= 5):
         total = total + 1
         if (elemento >= 7):
            m = m + 1
      
   print(total - m)
   vet = array(eval(input("Proximo vetor: ")))