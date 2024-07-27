stroka = input()# ввод
powtor = 1# счетчик повторов
symbol = ''# то, что повторяется к примеру а=symbol powtor=3 --> a3
kolich = len(stroka)# считаем количество символов в строке
for i in range(1 , kolich):# перебираем символы в строке
    if stroka [i - 1] == stroka [i] :# если текущий символ такой же, как следующий, то
        powtor = powtor + 1# к счетчику повторов добавляем 1
    else:# иначе
        symbol = symbol + (stroka[i - 1] + str(powtor))# к символу из строки добавляем строчную цифру из счетчика повторов чтоб получилось вида а5
        powtor = 1# обнуляем
    if kolich: #если в строке символы есть
          symbol = symbol + (stroka[-1] + str(powtor)) # то
print(symbol)#