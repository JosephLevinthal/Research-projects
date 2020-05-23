Q1 = input("Questao 1 a/b/c/d/e?: ")
Q2 = input("Questao 2 a/b/c/d/e?: ")
Q3 = input("Questao 3 a/b/c/d/e?: ")
V = 0
if (Q1 == "a"):
	R = V + 1
else:
	R = V
if (Q2 == "b"):
		R2 = V + 1
else:
	R2 = V
if (Q3 == "c"):
	R3 = V + 1
else:
	R3 = V
print(R + R2 + R3)
