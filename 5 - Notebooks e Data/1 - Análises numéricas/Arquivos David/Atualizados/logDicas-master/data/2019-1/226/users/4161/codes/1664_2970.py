t = float(input("tempo de investimento em meses: "))
qf = 1000000 + 42000
q0 = 1500
i = (qf/q0)**(1/t) - 1
print(round(i, 5))
if (i <= 0.01):
	print("Real")
else:
	print("Irreal")