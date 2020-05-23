verba = float(input("verba:"))
qtickets = int(input("quantidade de tickets:"))
vtickets = float(input("valor do ticket:"))
pbusao = int(input("q de passe:"))
vpassebusao = float(input("valor do passe:"))

if(verba >= (qtickets* vtickets) + (pbusao*vpassebusao)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")