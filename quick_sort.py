import random

option = int(input("Введите '1' для работы из консоли / Введите '2' для работы с файлом\n"))
if option == 1:
    # Работа с терминалом
    n = int(input("Введите количество элементов массива: "))
    if n != 0:
        array = [i for i in map(int, input("Введите через пробел элементы массива: ").split())]
else:
    # Работа с файлом
    path = input("введите путь к файлу: ")
    with open(path, "r") as file:
        array = [int(i) for i in file.read().split()]
        n = array[0]
        array = array[1:]


def partition(index_1, index_2, x):
    index_low = -1
    index_x = -1
    for now in range(index_1, index_2):
        if array[now] < x and index_low == -1 and index_x == -1:  # case 1
            tmp = array[now]
            array[now] = array[index_1]
            array[index_1] = tmp
            index_low = index_1
        elif array[now] < x and index_low != -1 and index_x == -1:  # case 2
            if now - 1 == index_low:
                index_low += 1
            else:
                tmp = array[now]
                array[now] = array[index_low + 1]
                array[index_low + 1] = tmp
                index_low += 1
        elif array[now] < x and index_low == -1 and index_x != -1:  # case 3
            tmp = array[now]
            array[now] = array[index_x + 1]
            array[index_x + 1] = array[index_1]
            array[index_1] = tmp
            index_x += 1
            index_low = index_1
        elif array[now] < x:  # case 4
            tmp = array[now]
            array[now] = array[index_x + 1]
            array[index_x + 1] = array[index_low + 1]
            array[index_low + 1] = tmp
            index_low += 1
            index_x += 1
        elif array[now] == x and index_low == -1 and index_x == -1:  # case 1
            tmp = array[now]
            array[now] = array[index_1]
            array[index_1] = tmp
            index_x = index_1
        elif array[now] == x and index_low == -1 and index_x != -1:  # case 2
            if now - 1 == index_x:
                index_x += 1
            else:
                tmp = array[now]
                array[now] = array[index_x + 1]
                array[index_x + 1] = tmp
                index_x += 1
        elif array[now] == x and index_low != -1 and index_x == -1:  # case 3
            tmp = array[now]
            array[now] = array[index_low + 1]
            array[index_low + 1] = tmp
            index_x = index_low + 1
        elif array[now] == x:  # case 4
            if now - 1 == index_x:
                index_x += 1
            else:
                tmp = array[now]
                array[now] = array[index_x + 1]
                array[index_x + 1] = tmp
                index_x += 1

    if index_low == -1 and index_x != -1:
        p = index_x + 1
    else:
        p = index_low + 1
    return p


def quick_sort(start, end):
    x = random.choice(array[start:end])
    p = partition(start, end, x)
    if p != end and p - start != 1:
        quick_sort(start, p)
    if p != end and end - p != 1:
        quick_sort(p, end)


if n != 0:
    quick_sort(0, n)
    print(" ".join(map(str, array)))
