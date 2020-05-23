A = float(input("lado A:"))
B = float(input("lado B:"))
C = float(input("lado C:"))
 
if( A <= 0 or B <= 0 or C <= 0 ):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","invalido")
elif((A >= B + C) or (B >= A + C) or (C >= B + A)):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","invalido")
	
elif((A == B) and (B == C)):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","equilatero")
elif((A == B) or (B == C) or (C == A)):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","isosceles")
elif((A != B) and (B != C) and (C != A) ):
	print("Entradas:",A,",",B,",",C)
	print("Tipo de triangulo:","escaleno")