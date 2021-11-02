# Если в функцию передаётся кортеж, то посчитать длину всех его слов. 
# Если список, то посчитать кол-во букв и чисел в нём. 
# Число – кол-во нечётных цифр.
# Строка – кол-во букв. 
# Сделать проверку со всеми этими случаями. 
cort = ('asd', 'weqr', 'ghj', 'dfjh', 'vcxz', 'adsfasdf')
my_list = [1, 'daqwe', 'dgfb', 234, 4, 5, 'sdfg', 6, 'gsdfg']
num = 1243123415455678457832
my_str = 'lghhy2uasdfasdfaenf1rajnfoiasdjfkcjgbler32'


def proverka():
    a = input('Выберите, что проверять: cort/my_list/num/my_str\n')
    if a == 'cort':
        count_cort = 0
        for i in cort:
            count_cort += len(i)
        print(f'Длина всех слов в кортеже - {count_cort} символов')
    if a == 'my_list':
        count_num = 0
        count_letter = 0
        for i in my_list:
            b = str(i)
            if b.isdigit():
                count_num += 1
            else:
                count_letter += len(i)
        print(f'Количество букв в списке - {count_letter}\n'
              f'Количество чисел - {count_num}')
    if a == 'num':
        count_odd = 0
        c = list(str(num))
        for i in c:
            n = int(i)
            if n % 2 != 0:
                count_odd += 1
            else:
                continue
        print(f'В этом числе - {count_odd} нечетных цифр')
    if a == 'my_str':
        count = 0
        l = list(my_str)
        for i in l:
            b = str(i)
            if b.isdigit():
                continue
            else:
                count += len(i)
        print(f'В строке - {count} букв')

proverka()