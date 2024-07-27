figura = input()
if figura == 'треугольник' :
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif figura == 'прямоугольник' :
    a = float(input())
    b = float(input())
    print(a * b)
elif figura == 'круг' :
    r = float(input())
    print(3.14 * (r ** 2))