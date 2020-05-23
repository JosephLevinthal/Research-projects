pontoa =  float(input("Coordenada Xa:"))
pontoa1 = float(input("Coordenada Ya:"))
pontob =	 float(input("Coordenada Xb:"))
pontob1 = float(input("Coordenada Yb:"))
dab = (pontob-pontoa)**2
dab1 = (pontob1-pontoa1)**2
dab2 = dab+dab1
dab3 = dab2**0.5
print(round(dab3, 3))