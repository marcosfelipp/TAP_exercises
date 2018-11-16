def primo(i):
    for j in range(2,round(i)):
        if i%j == 0:
            return
    primos.append(i)

def calculate_primo(min, k):
    for i in range(min, k):
        primo(i)

def calculate(N_K):
    N, K = N_K.split(' ')
    minimo = 2
    if len(primos) > 1:
        if int(K) > primos[-1]:
            minimo = primos[-1] +1
    calculate_primo(minimo, int(K))
    q = 0
    for x in range(2,int(N)):
        for i in range(len(primos)):
            if x > primos[i]:
                continue
            if primos[i] % x == 0:
                q+=1

    return q

primos = []

n = int(input())

resposta = []

for j in range(n):
    resposta.append([calculate(input())])

print(resposta)