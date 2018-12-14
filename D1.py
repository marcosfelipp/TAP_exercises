op = ['+','-','*','/']

str_equacao = input().split(' ')
str_equacao.pop(-1)

for i in range(len((str_equacao))):
    if str_equacao[i] not in op:
        str_equacao[i] = str(int(str_equacao[i],13))
    elif str_equacao[i] is '/':
        str_equacao[i] = '//'

equacao = ''
for i in str_equacao:
    equacao = equacao + i

print(eval(equacao))