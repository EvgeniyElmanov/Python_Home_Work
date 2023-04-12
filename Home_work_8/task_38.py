'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию,
 и Вы должны реализовать функционал для изменения и удаления данных
 fghdsdfghg
'''

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
        return data

def write_file(file_name, data):
    with open(file_name, 'w') as file:
        file.writelines(data)

def change_file():
    phone_book = read_file(path_file)
    for index in phone_book:
        print(index)

    search1 = int(input('Для добавления нажмите ->{1}: Для поиска нажмите ->{2}: '))
    if search1 == 1:
        phone_book.append(input('Введите новый контакт:') + '\n')
    elif search1 == 2:
        search = input('Для поиска введите имя фамилию абонента: ')
        a = None
        for index, i in enumerate(phone_book):
            if search in i:
                print(i)
                a = index
                break
        else:
            print('Введенный вами контакт не существует!')
        if a is not None:
            changes = int(input('Для изменения нажмите{1}: Для удаления нажмите {2}: '))
            if changes == 1:
                phone_book[a] = input('Введите изменения: ') + '\n'
            elif changes == 2:
                phone_book.pop(a)
                print('Запись удалена!')

    write_file(path_file, phone_book)

path_file = r"Telephone_book.txt"
if __name__ == '__main__':
    change_file()
