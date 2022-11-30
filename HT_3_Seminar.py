"""
3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления    
"""

def dec_to_hex():
    number = int(input('Введите десятичное число: '))
    num_hex = hex(number).split('x')[-1]
    print(f'Представление числа {number} в шестнадцатиричной системе => {num_hex}')

dec_to_hex()

"""
3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
"""

def count_dots_say_OK(line):    # проверяет, сколько точек в строке
    count = 0
    for symbol in range(len(line)):
        if line[symbol] == '.':
            count +=1
    if count == 1:
        return True
    else:
        return False
    
def could_be_number(line):      # проверяет, можно ли сконвертировать данную строку в число
    number=""
    for i in range(len(line)):
        number=number+line[i]
    if count_dots_say_OK(line):
        number = number.replace('.', '')
        try:
            int(number)
            return True
        except:
            print('unconvertible symbols in line!')
    else:
        print('couldn\'t be a number')
        return False
    
def is_float(line):
    if count_dots_say_OK(line) and could_be_number(line):
        print('Это дробное число!')
    else:
        print('Ошибка, пробуйте ещё!')    

input_line = input('введите ваше число: ')
is_float(input_line)

"""
3.12    Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку
        между первой и последней буквой "о" из исходной строки. Если она только одна или её 
        нет - то сообщить, что буква "о" - одна или не встречается.
"""
text = input('Введите строку: ')
def reverse_substring_between_o(line):
    range_betw_o = line.rfind('o') - line.find('o')
    result=""
    if count_os(line) > 1:
        for i in range(line.find('o')+1, line.rfind('o')-1):
            result = result + line[i]
        print(f' развёрнутая подстрока: {result[::-1]}')
    else:
        print('недостаточно "о" в строке')
           
def count_os (line):
    count = 0
    for i in range(len(line)):
        if line[i]=='o':
            count+=1
    return count 

reverse_substring_between_o(text)