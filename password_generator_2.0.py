import secrets

numbers = [chr(i) for i in range(48, 58)]
alphabet_upp = [chr(i) for i in range(65, 91)]
alphabet_low = [chr(i) for i in range(97, 123)]
punctuation = [chr(i) for i in range(33, 48)]
all_symb = []


amount_of_passwords = int(input('How many passwords do you want to generate: '))

if amount_of_passwords <= 0:
    print("Please enter amount more than 0")

password_len = int(input("What lenght of password do you want to have: "))

if 8 <= password_len <= 16:
    pass
else:
    print('Password should be not less than 8 and not more than 16 symbols')

include_num = input('Do you want to include numbers? "Y" for Yes, "N" for No ')

if include_num == 'y' or include_num == 'Y':
    all_symb += numbers
elif include_num == 'n' or include_num == 'N':
    pass
else:
    print("Please enter 'y' or 'n'")


include_low = input('Do you want to include lower case? "Y" for Yes, "N" for No ')


if include_low == 'y' or include_low == 'Y':
    all_symb += alphabet_low
elif include_low == 'n' or include_low == 'N':
    pass
else:
    print("Please enter 'y' or 'n'")


include_upp = input('Do you want to include upper  case? "Y" for Yes, "N" for No ')


if include_upp == 'y' or include_upp == 'Y':
    all_symb += alphabet_upp
elif include_upp == 'n' or include_upp == 'N':
    pass
else:
    print("Please enter 'y' or 'n'") 



include_punc = input('Do you want to include punctuation? "Y" for Yes, "N" for No ')

if include_punc == 'y' or include_punc == 'Y':
    all_symb += punctuation
elif include_punc == 'n' or include_punc == 'N':
    pass
else:
    print("Please enter 'y' or 'n'") 




def generate_password(lenght, chars):
    password_lst = []
    for i in range(amount_of_passwords):
        password = ''.join(secrets.choice(all_symb) for i in range(password_len))
        password_lst.append(password)
    return password_lst


print(*generate_password(password_len, all_symb))
















