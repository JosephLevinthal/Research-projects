qa = int(input("votos para ambrosio"))
qd = int(input("votos para demelza"))
total = qa + qd
if qa > qd:
	m = "Ambrosio Rutra"
	m2 = qa / total * 100
else: 
	m = "Demelza Olecram"
	m2 = qd / total * 100
print(m)
print(round(m2, 2))