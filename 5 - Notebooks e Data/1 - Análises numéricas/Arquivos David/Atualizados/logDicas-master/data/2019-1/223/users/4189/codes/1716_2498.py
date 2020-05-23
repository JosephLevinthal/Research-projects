habA = int(input("habitantes da cidade A"))
habB = int(input("habitantes da cidade B"))
crescA = float(input("crecimento da cidade A"))
crescB= float(input("crecimento da cidade B"))

anos=0

while(habA<=habB):
	habA=habA+(habA*(crescA/100))
	habB=habB+(habB*(crescB/100))
	anos=anos+1
print(anos)
	
	