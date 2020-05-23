base = int(input("Qual o tamanho da bse: "))
for j in range(0, base):
    for i in range(0, base - j):
        print("*" , end = "")
    print("\n", end = "")    
for j in range(0, base):
    for i in range(0, j + 1):
        print("*", end = "")
    print("\n", end = "")