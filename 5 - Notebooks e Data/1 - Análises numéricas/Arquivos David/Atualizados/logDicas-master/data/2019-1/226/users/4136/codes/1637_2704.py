var1 = float(input("nota do aluno: "))
var2 = input("se merecer S ou N")
if (var2.upper() == "S"):
	na = var1 + (var1 * 0.1)
if (var2.upper() == "N"):
	na = var1
print(na)
	