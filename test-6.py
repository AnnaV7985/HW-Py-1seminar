ticket = int (input('Введи шесть цифр номера билета: ' ))
half1 =  (ticket //100000) + (ticket//10000)%10 + (ticket//1000)%10
half2 = (ticket//100)%10 + (ticket//10)%10 + (ticket//1)%10
if (half1 == half2):

    print(f'Поздравляю, это же счастливый билет!')

else: 
    print (f'Не повезло')
