import random
from pathlib import Path

def generate_passwords(n, length, letters, register, numbers, replaces, specials, dict):
    '''
    функция генерации множества паролей с заданными параметрами
    n = количество паролей
    length = длина паролей
    letters = используются ли буквы
    register = используется ли регистр (1-только верх, 2-только ниж, 3-оба) ! letters == True !
    numbers = используются ли цифры
    replaces = есть ли замены букв на цифры ! ((numbers and letters) or (dict != 0)) !
    specials = используются ли спец символы
    dict = используются ли слова (1-англ, 2-ру(англ раскладка), 3-оба)
    '''
    
    def generate_password(length, letters, register, numbers, replaces, specials, dict):
        alphabet = [] #алфавит алфавитов
        password = '' #строка с паролем
        if letters:
            if (register == 1): #up only
                alphabet.append(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
            if (register == 2): #down only
                alphabet.append(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
            if (register == 3): #up and down
                alphabet.append(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                alphabet.append(
                    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

        if numbers:
            alphabet.append(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

        if specials:
            alphabet.append([ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'])

        if dict == 1: #eng only
            alphabet.append([w for w in Path('dictionary_eng.txt').read_text(encoding="utf-8").replace("\n", " ").split()])
        if dict == 2: #ru only
            alphabet.append([w for w in Path('dictionary_ru.txt').read_text(encoding="utf-8").replace("\n", " ").split()])
        if dict == 3: #eng + ru
            alphabet.append([w for w in Path('dictionary_eng.txt').read_text(encoding="utf-8").replace("\n", " ").split()])
            alphabet.append([w for w in Path('dictionary_ru.txt').read_text(encoding="utf-8").replace("\n", " ").split()])

        #генерация пароля
        while len(password) < int(length):
            r = random.choice(random.choice(alphabet))
            while (len(r) > int(length) - len(password)):
                r = random.choice(random.choice(alphabet))
            password += r

        if replaces:
            password = password.replace('a', '4')
            password = password.replace('A', '4')
            password = password.replace('i', '1')
            password = password.replace('I', '1')
            password = password.replace('t', '7')
            password = password.replace('T', '7')
            password = password.replace('e', '3')
            password = password.replace('E', '3')
            password = password.replace('g', '6')
            password = password.replace('G', '6')
            password = password.replace('s', '5')
            password = password.replace('S', '5')
            password = password.replace('z', '2')
            password = password.replace('Z', '2')
            password = password.replace('b', '8')
            password = password.replace('B', '8')

        print (password) #вывод пароля, можно поменять на return password по надобности

    print("Ваши пароли:\n")
    for i in range (n):
        generate_password(length, letters, register, numbers, replaces, specials, dict)
