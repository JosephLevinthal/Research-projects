from numpy import*
iglic = array(eval(input("digite os niveis de glicose: ")))
c = 0
x = 0
while(x<size(iglic)):
	if(iglic[x]>99):
		print(x)
		c = c + 1
	x = x + 1
print(c)