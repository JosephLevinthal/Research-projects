cash=float(input());
quantidade=int(input())
vtickt=float(input());
qonibus=int(input())
vpasse=float(input())

if(quantidade*vtickt+qonibus*vpasse>cash):
	print("INSUFICIENTE")
if(quantidade*vtickt+qonibus*vpasse<=cash):
	print("SUFICIENTE")