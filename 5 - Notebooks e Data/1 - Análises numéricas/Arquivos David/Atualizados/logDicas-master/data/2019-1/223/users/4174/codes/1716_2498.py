A = int(input("n de hab de A:"))
B = int(input("n de hab de B:"))
pcA = float(input("porcentagem de a:"))
pcB = float(input("porc de b:"))

anos = 0  #anospassados

while( A < B):
	A =  A + (A * pcA)/100  
	B = B + (B * pcB)/100
	anos = anos + 1
print(anos)
	
	
	
	




