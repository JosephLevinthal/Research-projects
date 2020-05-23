qi = int(input("Quantidade Inicial da Infantaria: "))
qc = int(input("Quantidade Inicial da Cavalaria: "))
pi = float(input("Percentual de Crescimento da Infantaria: "))/100
pc = float(input("Percentual de Crescimenro da Cavalaria: "))/100

meses = 1
infant = 1
cavalaria = 1

while(infant < cavalaria):
	qi = qi + (qi * pi )
	qc = qc + (qc * pc)
	meses = meses + 1
	infant = infant + qi
	cavalaria = cavalaria + qc 
	
	
	

  
	
	
	
	
	
	
	

		
	
	
	
