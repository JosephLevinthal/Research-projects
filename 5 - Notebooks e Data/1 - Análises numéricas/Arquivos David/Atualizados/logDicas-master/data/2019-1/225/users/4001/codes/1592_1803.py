num = float(input("Sequencia: "))
X = num // 1000
x = num % 1000
Y = x // 100
y = x % 100
Z = y // 10
z = y % 10
W = z

exp1 = W * 2  
exp2 = Z * 3
exp3 = Y * 4
exp4 = X * 5

D1 = (exp1 + exp2 + exp3 + exp4)% 11

print(int(D1))