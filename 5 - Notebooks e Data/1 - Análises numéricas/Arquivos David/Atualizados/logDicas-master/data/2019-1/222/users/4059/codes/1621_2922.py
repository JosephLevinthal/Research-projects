Qo=1500
Qf=1042000
t=int(input())
i=((Qf/Qo)**(1/t)) - 1

print("{:.5f}".format(i))