from numpy import*

vet = array(eval(input("Primeiro vetor: ")))

while (size(vet) > 1 ):
   mon = 0
   for elemento in vet:
      if (elemento >=5 and elemento <7 ):
         mon = mon + 1
		
		
   print(mon)


   # Leitura do proximo vetor
   vet = array(eval(input("Proximo vetor: ")))
