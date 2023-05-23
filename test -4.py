total = int (input ('введи общее число журавликов '))
Sergei = int (total/3)//2
Petr =  int (total/3)//2
Kate = int (Sergei + Petr ) * 2
print (f'{total} {Sergei, Kate, Petr}')
print (f'из {total} журавликов: Сергей сделал: {Sergei}, Катя сделала: { Kate}, Петр сделал {Petr}')