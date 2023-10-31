import random
import array

max_len = 12
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
locase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                     'n', 'o', 'p', 'q', 'r', 's', 
                     't', 'u', 'v', 'w', 'x', 'y', 'z']
upcase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
                     'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
                     'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '_', '[',
    ']', '{', '}', '|', '\\', ':', ';', ',', '.', '<', '>', '/', '?', "'", '"', '~']

combined_list = digits + locase_characters + upcase_characters + symbols   # Объединение всех символов в 1 список #

rand_digit = random.choice(digits)
rand_local = random.choice(locase_characters)
rand_upper = random.choice(upcase_characters)
rand_symbol = random.choice(symbols)

temp_pass = rand_digit + rand_local + rand_upper + rand_symbol  # Генерируются 4 символа пароля #

for x in range(max_len - 4):                             
    temp_pass = temp_pass + random.choice(combined_list)   # Генерируются остальные символы пароля, т.к 4 уже есть #

    temp_pass_list = array.array('u',temp_pass)   # список символов, представляющего собой temp_pass #    
    random.shuffle(temp_pass_list)               # Перемешивает символы в случайном порядке #

password = ""
for x in temp_pass_list:      # добавление в пароль перемешанных символов #
    password += x

print(password)