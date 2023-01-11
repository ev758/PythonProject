import sys

def print_menu():
    print('MENU')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')

def execute_menu(user_choice, sample_txt):
    if (user_choice == 'c'):
        get_num_of_non_WS_characters(sample_txt)

    elif (user_choice == 'w'):
        get_num_of_words(sample_txt)

    elif (user_choice == 'f'):
        fix_capitalization(sample_txt)

    elif (user_choice == 'r'):
        replace_punctuation(sample_txt, exclamation_count = 0, semicolon_count = 0)

    elif (user_choice == 's'):
        shorten_space(sample_txt)

    elif (user_choice == 'q'):
        quit_menu()


def get_num_of_non_WS_characters(sample_txt):
    num_of_non_WS_characters = 0
    
    for character in sample_txt:
        if (character.isspace()):
            continue
        else:
            num_of_non_WS_characters += 1
    return print('Number of non-whitesapce characters:', num_of_non_WS_characters)


def get_num_of_words(sample_txt):
    number_of_words = len(sample_txt.split())
    return print('Number of words:', number_of_words)


def fix_capitalization(sample_txt):
    new_sample_txt = ''
    num_of_letters_capitalized = 0
    
    for x in range(len(sample_txt)):
        if (sample_txt[x].islower()):
            new_sample_txt = new_sample_txt + sample_txt[x].upper()
            num_of_letters_capitalized += 1
        else:
            new_sample_txt = new_sample_txt + sample_txt[x]
    print('Number of letters capitalized:', num_of_letters_capitalized)
    return print('Edited text:', new_sample_txt)

def replace_punctuation(sample_txt, exclamation_count, semicolon_count):
    sample_txt2 = ''
    for character in sample_txt:
        if (character == '!'):
            character = '.'
            sample_txt2 += character
            exclamation_count += 1
        elif (character == ';'):
            character = ','
            sample_txt2 += character
            semicolon_count += 1
        else:
            sample_txt2 += character
    print('Punctuation replaced')
    print('exclamation_count:', exclamation_count)
    print('semicolon_count:', semicolon_count)
    return print('Edited text:', sample_txt2)


def shorten_space(sample_txt):
    if (not sample_txt.isspace()):
        sample_txt = ' '.join(sample_txt.split())
    return print('Edited text:', sample_txt)


def quit_menu():
    print('\nExiting menu')
    sys.exit()

def main():
    x = True
    while (x == True):
        sample_txt = input('Enter a sample text:\n')
        print('\n')
        print('You entered:', sample_txt)
        print('\n')
        print_menu()
        user_choice = input('Choose an option: ')
    
        while (x == True):
            if (user_choice == 'c'):
                execute_menu(user_choice, sample_txt)
                print('\n')
                print_menu()
                print('Choose another option after entering sample text.')
                break
    
            elif (user_choice == 'w'):
                execute_menu(user_choice, sample_txt)
                print('\n')
                print_menu()
                print('Choose another option after entering sample text.')
                break
        
            elif (user_choice == 'f'):
                execute_menu(user_choice, sample_txt)
                print('\n')
                print_menu()
                print('Choose another option after entering sample text.')
                break
        
            elif (user_choice == 'r'):
                execute_menu(user_choice, sample_txt)
                print('\n')
                print_menu()
                print('Choose another option after entering sample text.')
                break
        
            elif (user_choice == 's'):
                execute_menu(user_choice, sample_txt)
                print('\n')
                print_menu()
                print('Choose another option after entering sample text.')
                break
        
            elif (user_choice == 'q'):
                execute_menu(user_choice, sample_txt)
                break
        
            else:
                user_choice = input('Choose an option: ')

main()