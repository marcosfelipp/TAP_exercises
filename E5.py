import math

n = int(input())
bac1 = input().split(' ')
bac2 = input().split(' ')

forces1 = [math.log(int(i)) for i in bac1]
forces2 = [math.log(int(i)) for i in bac2]

force1 = 0
force2 = 0

for f in forces1:
	force1 += f

for f in forces2:
	force2 += f

if force1 > force2:
	print("A")
else:
	print("B")
