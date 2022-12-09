# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from random import randint
import time

field_size = 10  # размер поля
limit_3 = 1
limit_2 = 2
limit_1 = 3
stand_user = 0  # счёт игрока
stand_comp = 0  # счёт компа
count_3_ship = 0  # кол-во 3 палубных кораблей игрока
count_2_ship = 0  # кол-во 2 палубных кораблей игрока
count_1_ship = 0  # кол-во 1 палубных кораблей игрока
helping_flag = True
count = 0

upper_coordinates = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']
sea = [['-' for _ in range(field_size + 1)]
       for _ in range(field_size + 1)]  # поле игрока
sea_comp = [['-' for _ in range(field_size + 1)]
            for _ in range(field_size + 1)]  # поле компа
sea_shot = [['-' for _ in range(field_size + 1)]
            for _ in range(field_size + 1)]  # поле выстрелов игрока

# хранит выстрелы компа со всех раундов
dic_previous_rnds = {a: 0 for a in range(field_size ** 2)}


# текущий счётчик словаря dic_previous_rnds


def output_user(field):  # вывод поля в консоль
    print('Ваше поле: ')
    for i in range(len(field)):
        for j in range(len(field)):
            print(field[i][j], end=' ')
        print()


def output_comp(field):  # вывод поля в консоль
    print('Поле компа: ')
    for i in range(len(field)):
        for j in range(len(field)):
            print(field[i][j], end=' ')
        print()


def output_shot(field):  # вывод поля в консоль
    print('Ваши выстрелы: ')
    for i in range(len(field)):
        for j in range(len(field)):
            print(field[i][j], end=' ')
        print()


def create_coordinates(field):  # добавление координат полю
    for i in range(1, field_size + 1):
        field[0][i] = upper_coordinates[i - 1]
    for j in range(1, field_size + 1):
        field[j][0] = str(j) + '\t|'
    field[0][0] = '_\t|'


# вспомогательная функция: ищет номер строки в массиве для создания кораблей
def search_column_vec(matrix, search_str):
    for i in range(1, field_size + 1):
        if matrix[i][0] == search_str + '\t|':
            return i


# создает корабли: 1-, 2-, 3-палубный по координатам в формате А-2, Б-4 и т.д.
def create_ship():
    try:
        x = input(
            f'Введите координату х в формате: {[upper_coordinates[i] for i in range(0, field_size)]}: ')
        y = input(
            f'Введите координату y в формате: {[i for i in range(1, field_size + 1)]}: ')
        size = int(input('Введите размер корабля (1, 2 или 3):\t'))
        index_x = sea[0].index(x)
        index_y = search_column_vec(sea, y)
        for i in range(index_y, index_y + size):
            sea[i][index_x] = 'X'
        return size
    except:
        print('Ошибка! Корабль не влезает в игровое поле!')


def create_ship_comp():
    count_3s_comp = 0
    count_2s_comp = 0
    count_1s_comp = 0

    while count_3s_comp < limit_3:
        x_coord = randint(1, field_size - 3)
        y_coord = randint(1, field_size - 1)
        if sea_comp[x_coord][y_coord] != 'X' and sea_comp[x_coord - 1][y_coord] != 'X' and sea_comp[x_coord + 2][
            y_coord] != 'X' \
                and sea_comp[x_coord][y_coord - 1] != 'X' and sea_comp[x_coord][y_coord + 1]:
            for j in range(x_coord, x_coord + 3):
                sea_comp[j][y_coord] = 'X'
            count_3s_comp = count_3s_comp + 1

    while count_2s_comp < limit_2:
        x_coord = randint(1, field_size - 2)
        y_coord = randint(1, field_size - 1)
        if sea_comp[x_coord][y_coord] != 'X' and sea_comp[x_coord - 1][y_coord] != 'X' and sea_comp[x_coord + 2][
            y_coord] != 'X' \
                and sea_comp[x_coord][y_coord - 1] != 'X' and sea_comp[x_coord][y_coord + 1]:
            for j in range(x_coord, x_coord + 2):
                sea_comp[j][y_coord] = 'X'
            count_2s_comp = count_2s_comp + 1

    while count_1s_comp < limit_1:
        x_coord = randint(1, field_size - 1)
        y_coord = randint(1, field_size - 1)
        if sea_comp[x_coord][y_coord] != 'X' and sea_comp[x_coord - 1][y_coord] != 'X' and sea_comp[x_coord + 1][
            y_coord] != 'X' \
                and sea_comp[x_coord][y_coord - 1] != 'X' and sea_comp[x_coord][y_coord + 1]:
            sea_comp[x_coord][y_coord] = 'X'
            count_1s_comp = count_1s_comp + 1


def combs(field):
    d = {a: (0, 0) for a in range(field_size ** 2)}
    counter = 0
    for i in range(1, field_size + 1):
        for j in range(1, field_size + 1):
            d[counter] = (i, j)
            counter += 1
    return d


def shoot_reached_or_not():  # выстрелы компа.
    global count
    rnd_key = randint(1, 99)
    # гоняет генератор случайных чисел, пока не появится то которого не было
    while rnd_key in dic_previous_rnds.values():
        rnd_key = randint(1, 99)
    while rnd_key not in dic_previous_rnds.values():
        (x_shoot, y_shoot) = combins.pop(rnd_key)
        dic_previous_rnds[count] = rnd_key
        count = count + 1
        print(f'компьютер бьет по координатам: {upper_coordinates[x_shoot-1]}-{y_shoot}')
        time.sleep(3)
    if sea[x_shoot][y_shoot] == 'X':
        print('попадание!')
        sea[x_shoot][y_shoot] = 0
        output_user(sea)
        return True
    elif sea[x_shoot][y_shoot] == '-':
        print('Компьютер промахнулся!')
        output_user(sea)
        return False


def shoot():
    x = input(
        f'Введите координату х в формате: {[upper_coordinates[i] for i in range(0, field_size)]}:\t')
    y = input(
        f'Введите координату y в формате: {[i for i in range(1, field_size + 1)]}:\t')
    index_x = sea[0].index(x)
    index_y = search_column_vec(sea, y)
    if sea_comp[index_y][index_x] == 'X':
        print('Попадание! Поздравляем')
        sea_shot[index_y][index_x] = 0
        output_comp(sea_shot)
        return True
    elif sea_comp[index_y][index_x] == '-':
        print('Вы промахнулись!')
        sea_shot[index_y][index_x] = '*'
        output_comp(sea_shot)
        return False


create_coordinates(sea)
create_coordinates(sea_comp)
create_coordinates(sea_shot)
# хранит выстрелы компа со всех раундов
combins = combs(sea)
create_ship_comp()


while stand_comp < 10 and stand_user < 10:


    while count_1_ship < limit_1 or count_2_ship < limit_2 or count_3_ship < limit_3:
        output_user(sea)
        print('Создайте ваши корабли')
        shiptype = create_ship()
        if shiptype == 3:
            count_3_ship += 1
        elif shiptype == 2:
            count_2_ship += 1
        elif shiptype == 1:
            count_1_ship += 1
        else:
            print('Error!')

    helping_flag = True
    print(f'начало игры! счёт: {stand_user}: {stand_comp}')
    print('Ваш ход!')

    output_shot(sea_shot)

    while helping_flag:  # стреляет игрок
        if shoot():
            stand_user = stand_user + 1
            if stand_user == 10:
                print(f'Игра окончена, вы победили! \n Счёт: {stand_user} : {stand_comp}')
                break
            print(f'Счёт:\t{stand_user} : {stand_comp}')
            print('Еще один выстрел')
        else:
            print('Стреляет компьютер')
            helping_flag = False

    helping_flag = True

    while helping_flag:  # стреляет комп
        if shoot_reached_or_not():
            stand_comp = stand_comp + 1
            if stand_comp == 10:
                print(f'Игра окончена, компьютер победил! \n Счёт: {stand_user} : {stand_comp}')
                break
            print(f'Счёт:\t{stand_user} : {stand_comp}')
            print('Еще один выстрел')
        else:
            helping_flag = False
