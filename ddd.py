print('введите операции через ентер - число-операция-число')
a = float(input())
b = (input())
c = float(input())
#d = (input())
if b == '+':
    print(float(a) + float(c))
elif b == '-':
    print(float(a) - float(c))
elif b == '/':
    if c == 0:
        print('Деление на 0!')
    else :
        print(float(a) / float(c))

elif b == '*':
    print(float(a) * float(c))
elif b == 'mod':
    if c == 0:
        print('Деление на 0!')
    else:
        print(float(a) % float(c))
elif b == 'pow':
    print(pow(float(a), float(c)))
elif b == 'div':
    if c == 0:
        print('Деление на 0!')
    else:
        print(float(a) // float(c))