n = int(input())
vet = []
for i in range(n):
    vet.append(int(input()))
count = 0
for i in range(n):
    if vet[i] == 2 or vet[i] == 3:
        count +=1
print(count)