N = int(input())

x_y_vigas = []
vigas_vistas = []
qtd_vigas = 1

for i in range(N):
    x_y_vigas.append(input().split(' '))

# Add primeira viga
vigas_vistas.append([int(x_y_vigas[0][0]), int(x_y_vigas[0][1])])

for i in range(1,N):
    var = 1
    for viga in vigas_vistas:
        # Verifico se ha interceccao entre as vigas
        if (int(x_y_vigas[i][0]) >= viga[0] and int(x_y_vigas[i][0]) <= viga[1]) or (int(x_y_vigas[i][1]) >= viga[0] and int(x_y_vigas[i][1]) <= viga[1]):
            viga[0] = int(x_y_vigas[i][0]) if int(x_y_vigas[i][0]) < viga[0] else viga[0]
            viga[1] = int(x_y_vigas[i][1]) if int(x_y_vigas[i][1]) > viga[1] else viga[1]
            var = 0
            break
    if var == 1:
        vigas_vistas.append([int(x_y_vigas[i][0]), int(x_y_vigas[i][1])])
        qtd_vigas+=1

print(qtd_vigas)
for viga in vigas_vistas:
    print(str(viga[0]) + ' ' + str(viga[1]))