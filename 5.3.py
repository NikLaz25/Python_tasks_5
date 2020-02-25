'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.'''

with open('text3.1.txt', 'rt') as my_f:
    zp = []
    ilines = my_f.readlines()
    for i in ilines:
        key, val = i.split(' - ') # освоил новый приём split(' - '), спасибо
        zp.append(int(val))
        if int(val) < 20000:
            print('Зп меньше чем 20 тыс: ', key)
    print('Средняя зп: ', sum(zp)/len(zp))
    # dict1 = dict(key[i]: val[i])
my_f.close()
# with open('text3.1.txt') as f:
#     salaries = []
#     lines = f.readlines()
#     for line in lines:
#         name, salary = line.split(' - ')
#         salaries.append(int(salary))
#         if int(salary) < 20000:
#             print(line, end='')
#     print('\nСредняя зп:', sum(salaries) / len(salaries))
    # print(ilines)
    # print(ilines[1])
#     for i, n in enumerate(istr, 1):
#         print(f'Номер строки: {i}, Символов в строке: {len(n) - 1}')  #