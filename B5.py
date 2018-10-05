n, r = input().split(' ')
pcs = []

for i in range(int(n)):
	a, b = input().split(' ')
	pcs.append([int(a), int(b)])

r = int(r)
pcs = sorted(pcs)
qtd = 0

for pc in pcs:
	preco, quantidade = pc
	itens = ((r/preco) if r/preco < quantidade else  quantidade)
	qtd = qtd + itens
	r -= itens * preco

print(int(qtd))
