def menu():
    print('1. Распечатать справочник.\n'
          '2. Найти телефон по фамилии.\n'
          '3. Изменить номер телефонаю.\n'
          '4. Удалить запись.\n'
          '5. Добавить абонент в справочник.\n'
          '6. Копирования данных из одного справочника в другой.\n'
          '7. Закончить работу.' )

    number = int(input('Введите номер из меню: '))
    return number

def work_with_phonebook():
    number = menu()
    phonebook = read_csv('phonebook.csv')
    while (number !=7):
        if number == 1:
            print_phonebook(phonebook)
        elif number == 2:
            sur_name = input('Ведите фамилию: ')
            surname(sur_name, phonebook)
        elif number == 3:
            surname = input('У кого хотите изменить номер? ')
            new_number = input('Введите новый номер телефона: ')
            newnumber(surname, new_number, phonebook, 'phonebook.csv')
        elif number == 4:
            surname = input('Кого вы хотите удалить? ')
            delete(surname, phonebook, 'phonebook.csv')
        elif number == 5:
            add_user(phonebook, 'phonebook.csv')
        elif number == 6:
            copy_user(phonebook, surname= input("Укажите фалимию кого вы хотите скопировать:"))

        number = menu()
        
    print('Работа закончена!')

def read_csv(filename):
    phone_book =[]
    fileds = ['Фамилия', 'Имя', 'Номер', 'Описания']
    with open(filename, 'r', encoding= 'utf-8') as phb:
        for line in phb:
            record = dict(zip(fileds, line.split(',')))
            phone_book.append(record)
    print(phone_book)
    return phone_book

def print_phonebook(phonebook):
    fileds = ['Фамилия', 'Имя', 'Номер', 'Описания']
    print(','.join(fileds))
    print()
    for slov in phonebook:
        asd =[]
        for i in fileds:
            asd.append(str(slov[i]))
        print(', '.join(asd))

def surname(im, phonebook):
    for slov in phonebook:
        if slov['Фамилия'] == im:
            return print(f"Номер {slov['Фамилия']} {slov['Имя']}: {slov['Номер']}") 
    return print(f'Абонент {im} не найдет')
    
def newnumber(surname, new_namber, phonebook, filename):
    for slov in phonebook:
        if slov['Фамилия'] == surname:
            slov['Номер'] = new_namber
            write_txt(filename , phonebook)
            return phonebook       
    return print(f'Абонент {surname} не найдет')

def write_txt(filename , phone_book):
    with open('phonebook.csv','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}')

def delete(surname, phonebook, filename):
    i=-1
    for slov in phonebook:
        i+=1
        if slov['Фамилия'] == surname:
            phonebook.pop(i)
            return write_txt(filename , phonebook)
    print(f'Абонент {surname} не найдет')


def add_user(phonebook, filename):
    fileds = ['Фамилия', 'Имя', 'Номер', 'Описания']
    s ={}
    for i in fileds:
        s[i] = input(f'Введите {i} : ')
    phonebook.append(s)
    write_txt(filename , phonebook)
    
def copy_user(phonebook, surname):
    for slov in phonebook:
        if slov['Фамилия'] == surname:
            with open(input('Введите имя файла(без расширения): ')+'.csv','w',encoding='utf-8') as phout:
                s = ''
                for v in slov:    
                    s += slov[v]+ ', '
                return phout.write(f'{s[:-1]}')
    print(f'Абонент {surname} не найдет')

work_with_phonebook()