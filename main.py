# Программа на нахождение размера брюк.
higt=float(input('Какой у вас рост? '))
hip=float(input('Какой у вас обхват бедер? '))
if higt < 150:
     if 75 <= hip < 80:
       print('Размер 1')
     elif 80 <= hip <= 85:
       print('Размер 2')
     elif 85 < hip <= 90:
       print('Размер 3')
     else:
       print('Размер 4')
elif 150 <= higt < 170:
     if 75 <= hip < 80:
       print('Размер 5')
     elif 80 <= hip <= 85:
       print('Размер 6')
     elif 85 < hip <= 90:
       print('Размер 7')
     else:
       print('Размер 8')
elif 170 <= higt <= 190:
    if 75 <= hip < 80:
        print('Размер 9')
    elif 80 <= hip <= 85:
        print('Размер 10')
    elif 85 < hip <= 90:
        print('Размер 11')
    else:
        print('Размер 12')
else:
  print('Размер 13')