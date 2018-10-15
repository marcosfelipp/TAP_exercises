from math import log

v1, v2 = input().split(' ')
qtd_max_melancias = float(v2) / float(v1)

camadas = int(log(qtd_max_melancias, 3))

if 3**camadas + 1 > int(qtd_max_melancias):
	camadas -= 1

print(camadas)
