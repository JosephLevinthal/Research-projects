valor = float(input())

qtdRU = int(input())
valorTicket = float(input())

qtdPasses = int(input())
valorPasses = float(input())

totalRu = qtdRU * valorTicket

totalPasses = qtdPasses * valorPasses

despesa = totalRu + totalPasses

if( valor > despesa):
		print('SUFICIENTE')
elif ( valor < despesa):
		print('INSUFICIENTE')