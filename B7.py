D = int(input())

dic = {'*...':1, '*.*.':2,'**..':3, '**.*':4, '*..*':5, '***.':6, '****':7,'*.**':8,'.**.':9,'.***': 0}

pt1 = [i for i in input().split(' ')]
pt2 = [i for i in input().split(' ')]
pt3 = input()

num = ''
for i in range(D):
    num += str(dic.get(pt1[i]+pt2[i]))

print(num)