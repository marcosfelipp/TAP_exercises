
def test_numbers(numbers):
    numbers = sorted(numbers)
    if numbers[0] == numbers[1] - 1 and numbers[1] == numbers[2] - 1:
        return 'consecutives'
    elif numbers[0] == numbers[1] and numbers[1] == numbers[2]:
        return 'equals'
    else:
        return 'differents'

def test_suits(cards):
    if (cards[0] == cards[1]) and (cards[1] == cards[2]): 
        return True
    else: 
        return False

def score(n, s):
    if n == 'consecutives' and s == True:
        return 100
    elif n == 'equals' and s == False:
        return 80
    elif n == 'differents' and s == True:
        return 60
    elif n == 'consecutives' and s == False:
        return 40
    else:
        return 0

def verify_tie(number_1, number_2):
    sum_1 = number_1[0] + number_1[1] + number_1[2]
    sum_2 = number_2[0] + number_2[1] + number_2[2]
    if sum_1 > sum_2:
         print('Player 1 wins.')
    elif sum_1 < sum_2:
         print('Player 2 wins.')
    else:
        print('There is a tie.')
    
cards = input().split(' ')
cards_1 = [ cards[i] for i in range(3)]
cards_2 = [ cards[i] for i in range(3,6)]

n1 = test_numbers([int(cards_1[i][0]) for i in range(3)])
n2 = test_numbers([int(cards_2[i][0]) for i in range(3)])

s1 = test_suits([cards_1[i][1] for i in range(3)])
s2 = test_suits([cards_2[i][1] for i in range(3)])

score1 = score(n1, s1)
score2 = score(n2, s2)

if score1 > score2:
    print('Player 1 wins.')
elif score1 < score2:
    print('Player 2 wins.')
else:
    verify_tie([int(cards_1[i][0]) for i in range(3)], [int(cards_2[i][0]) for i in range(3)])