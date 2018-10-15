n = int(input())
bolas = input().split(' ')

result = 0
for bola in bolas:
	if int(bola) % 2 != 0:
		result +=int(bola)

if result%2 != 0:
	print('S')
else:
	print('N')
