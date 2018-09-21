def consulta_caminho(estacao1, estacao2, tem_tunel):
    caminho = []
    while(atual[1] != estacao2):
        
        if 
    return caminho

def calcula_estacoes(consulta, tem_tunel):
    estacoes_em_comum = 0
    caminho1 = consulta_caminho(int(consulta[0]), int(consulta[1]), tem_tunel)
    caminho2 = consulta_caminho(int(consulta[2]), int(consulta[3]), tem_tunel)
    for estacao in caminho1:
        if estacao in caminho2:
            estacoes_em_comum += 1
    return estacoes_em_comum

n, q = input().split(' ')
tem_tunel = [[ 0 for i in range(int(n))] for j in range(int(n))]
consultas = []
for i in range(int(n)-1):
    tunel = input().split(' ')
    tem_tunel[int(tunel[0])-1][int(tunel[1])-1] = 1
    tem_tunel[int(tunel[1])-1][int(tunel[0])-1] = 1
for i in range(int(q)):
    consultas.append()

for consulta in consultas:
    print(calcula_estacoes(consulta, tem_tunel))