def quadrante(n, x , y):
    if x <= n/2 and y <= n/2:
        return 1
    if x <= n/2 and y > n/2:
        return 2
    if x > n/2 and y <= n/2:
        return 3
    if x > n/2 and y > n/2:
        return 4

n = int(input())
x1, y1 = input().split(' ')
x2, y2 = input().split(' ')

q1 = quadrante(n, int(x1), int(y1))
q2 = quadrante(n, int(x2), int(y2))

if q1 != q2:
    print("S")
else:
    print("N")