'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.'''

with open('text1.txt', 'rt') as my_f:
    istr = my_f.readlines()
    print('Всего строк: ', len(istr))
    for i, n in enumerate(istr, 1):
        print(f'Номер строки: {i}, Символов в строке: {len(n)-1}') # Непонятно почему len считает на 1 больше. ПРишлось вычесть
my_f.close()



            # my_f = split(my_f)
    #
    # x = 1
    # for i, n in enumerate(my_f):
    #     print(i, len(n))
    #     x += 1
    # print(x)
    # my_f.close()






# my_f = open('text1.txt', 'a')
# while 1:
#     x = input('Введите строку: ' + '\n')
#     if x == '':
#         print(my_f)
#         break
#     my_f.write(x + '\n')
# # my_f = open('text1.txt', 'r')
# # print(my_f.read())
# my_f = split(my_f())
# x = 1
# for i, n in enumerate(my_f):
#     print(i, len(n))
#     x += 1
# print(x)
# my_f.close()