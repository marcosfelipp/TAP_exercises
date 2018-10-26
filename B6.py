saques = input().split(' ')
qtd_saques = int(saques.pop(0))

points_a = 0
points_b = 0

anterior = 'A'
while(len(saques) > 0):
    saque = saques.pop(0)
    if saque == anterior:
        if saque == 'A':
            points_a+=1
        else:
            points_b+=1
    if points_a >= 15 and points_a > points_b+1:
        print('Team A has won the match with a score of ' + str(points_a) + '-' + str(points_b) + '.')
        exit()
    if points_b >= 15 and points_b > points_a+1:
        print('Team B has won the match with a score of ' + str(points_a) + '-' + str(points_b) + '.')
        exit()
    anterior = saque

print('The score is ' + str(points_a) + '-' + str(points_b) + '.')