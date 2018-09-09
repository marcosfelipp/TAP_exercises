def sign(p1, p2, p3):
    return float(p1[0] - p3[0]) * float(p2[1] - p3[1]) - (p2[0] - p3[0]) * float(p1[1] - p3[1])

def point_in_triangle(pt, v1, v2, v3):

    b1 = sign(pt, v1, v2) < 0
    b2 = sign(pt, v2, v3) < 0
    b3 = sign(pt, v3, v1) < 0
    return ((b1 == b2) and (b2 == b3))

def test_cord(v11, v12, v13, v21, v22, v23):
    score = 0
    score = score + 1 if point_in_triangle(v11,v21,v22,v23) is True else score
    score = score + 1 if point_in_triangle(v12,v21,v22,v23) is True else score
    score = score + 1 if point_in_triangle(v13,v21,v22,v23) is True else score

    return score

cord = input().split(' ')
cord = [int(i) for i in cord]
n1 = test_cord([cord[0],cord[1]],[cord[2],cord[3]],[cord[4],cord[5]], [cord[6],cord[7]],[cord[8],cord[9]],[cord[10],cord[11]])
n2 = test_cord([cord[6],cord[7]],[cord[8],cord[9]],[cord[10],cord[11]], [cord[0],cord[1]],[cord[2],cord[3]],[cord[4],cord[5]])

if n1 == n2:
    print('Both claims have equal numbers of intruding points: ' + str(n1))
else:
    string = 'Claim ' + ('1' if n1 > n2 else '2') + ' has ' + (str(n1) if n1 > n2 else str(n2)) + ' vertices inside Claim' + (' 2.' if n1 > n2 else ' 1.')
    print(string)

