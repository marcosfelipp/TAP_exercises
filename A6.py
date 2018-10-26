R, S, G = input().split(' ')
grupos = input().split(' ')

qtd_fileiras = [int(S) for i in range(int(R))]
grupos = [int(i) for i in grupos]
x = 0
S = int(S)

# Para cada grupo:
while(len(grupos) > 0):
    grupo = int(grupos.pop(0))
    # excede limite da fielira
    if grupo > S:
        x+=1
    else:
        set_x = 1
        # Percorre cada fileira procurando um espaco vazio
        for i in range(int(R)):
            if grupo <= qtd_fileiras[i]:
                qtd_fileiras[i]-= grupo
                set_x = 0
                break
        if set_x == 1:
            x+=1
if x == 0:
    print('All groups got tickets.')
else:
    print(str(x) + ' of the ' +  str(G) + ' groups did not get tickets.')
