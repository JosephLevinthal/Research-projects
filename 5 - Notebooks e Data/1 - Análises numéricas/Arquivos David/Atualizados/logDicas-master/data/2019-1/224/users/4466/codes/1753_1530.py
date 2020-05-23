q1 = int(input("quantidade inicial de pergaminhos:"))
q2 = int(input("quantidade inicial de varinhas:"))
p1 = float(input("percentual 1:"))
p2 = float(input("percentual 2:"))

cont = 0

while(q1 + q2 < 80000):
	q1 = q1 + (q1 * p1/100)
	q2 = q2 + (q2 * p2/100)
	cont = cont + 1
print(cont)
     