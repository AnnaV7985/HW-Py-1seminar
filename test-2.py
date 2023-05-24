




number = int (input('Введи трехзначное число ' ))
valueFirst =  (number //100) 
valueSecond = (number//10) % 10
valueTree =  (number-100) % 10
result = valueFirst +  valueSecond + valueTree
print (f'Сумма цифр числа {number} = {result} ({valueFirst}+{valueSecond}+{valueTree})')

