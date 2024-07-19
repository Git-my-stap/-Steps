a = input()
b = 0 # счетчик G
c = 0 # счетчик C
d = len(a)
for i in a :
    if i == 'c' or i == 'C' : # перебираем с
        c = c + 1
    if i == 'G' or i == 'g' : # перебираем ж
        b = b + 1
print(((c + b) / d) * 100)
