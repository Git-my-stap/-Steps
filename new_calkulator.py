#a,b,c = str (input('Введите пример '))
#float(a)
#float(c)
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

        #333333333333333333333333333333333333

a = float(input())
b = float(input())
c = (input())
if c == '+' :
    print(float(a) + float(b))
elif c == '-' :
    print(float(a) - float(b))
elif c == '/' :
    if b != 0:
        print(float(a) / float(b))
    else :
        print('Деление на 0!')
elif c == '*' :
    print(float(a) * float(b))
elif c == 'mod' :
    if b != 0 :
        print(float(a) % float(b))
    else :
        print('Деление на 0!')
elif c == 'pow' :
    print(float(a) ** float(b))
elif c == 'div' :
    if b != 0 :
        print(float(a) // float(b))
    else :
        print('Деление на 0!')