'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

with open('text4.1.txt') as my_f:
    ilines = my_f.readlines()
my_f.close()
with open('text4.2.txt', 'w') as my_f2:
    for i in ilines:
        if 'One' in i:
            i = i.replace('One','Один')
        if '2' in i:  #Оказалось необязательно использовать elif, оставил if всё работает
            i = i.replace('Two', 'Два')
        elif '3' in i:
            i = i.replace('Three', 'Три')
        elif '4' in i:
            i = i.replace('Four', 'Четыре')
        my_f2.write(i)
        print(i, end='')
my_f2.close()



