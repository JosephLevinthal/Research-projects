n1 = int(input("N1"))
n2 = int(input("N2"))
n3 = int(input("N3"))

var1 = min(n1, n2, n3)
var2 = max(n1, n2, n3)
var3 = n1 + n2 + n3 - (var1 + var2)
print(var3)