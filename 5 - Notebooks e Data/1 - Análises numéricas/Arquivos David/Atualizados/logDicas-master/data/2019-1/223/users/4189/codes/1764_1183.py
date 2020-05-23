from numpy import * 
vetor = array(eval(input("vetor:")))
v = array([ x for x in vetor if x>0 ])
print(v)