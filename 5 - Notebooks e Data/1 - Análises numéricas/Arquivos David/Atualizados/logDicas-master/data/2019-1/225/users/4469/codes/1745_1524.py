qi = int(input())
x = int(input())
y = int(input())

t = 0

while(qi > 0):
	qi = qi + x - y
	t = t + 1

print(t)