sel = float(input("sel:"))
s = float(input("s:"))
sob= float(input("sob:"))

prato= 26.90
suco=3.50
sobremessa= 3.00

total= sel*prato/1000 + s*suco +  sob*sobremessa
print(round(total,2))