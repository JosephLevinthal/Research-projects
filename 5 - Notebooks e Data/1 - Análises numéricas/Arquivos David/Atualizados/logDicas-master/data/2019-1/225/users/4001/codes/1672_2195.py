data = int(input("Data: "))
DD = data //1000000
MM = (data % 1000000) // 10000
A = data % 10000

if (A > 0) and (MM >= 1) and (MM <= 12) and (DD >= 1)