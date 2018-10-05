n , k = input().split(' ')
numeros = input().split(' ')

numeros = [ int(i) for i in numeros]

for i in range(int(k)):
	menor = 999999
	pos_menor = 0
	for i in range(int(n)):
		if numeros[i] < menor:
			menor = numeros[i]
			pos_menor = i
	numeros[pos_menor] = numeros[pos_menor] * -1

sum = 0
for i in range(int(n)):
	sum += numeros[i]

print(sum)
