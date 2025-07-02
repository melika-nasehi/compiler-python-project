import pandas as pan
import numpy as np
from numpy.ma.core import array

csv_path = "DFAtoTable_Compiler1.csv"
token_list = []

#reading the DFA table from excel(csv) file
def read_csv_file(csv_path) :
    DFA_table = pan.read_csv(csv_path)
    column = DFA_table.columns.to_numpy()
    column = np.delete(column , 0)

    column[67] = ' '
    column[69] = '\n'
    column[70] = '\t'
    column[71] = '\v'
    column[72] = '\r'
    column[73] = '\f'
    DFA_array = np.array(DFA_table)
    DFA_array = DFA_array[:,1:]


    return DFA_array, column

program_path = "cprogram.c"

def count(file_path) :
    line_number = 1
    with open(file_path, 'r') as file:
        for line in file:
            print("line : " ,line_number)
            line_number += 1




# adding the alphabet column
def find_index(input_char, column):
    for i, char in enumerate(column):
        if char==input_char:
            return i

'''def lexer(program , DFA_array, column):
    current_state = 0
    file = open(program, 'r')
    token = ''
    char = ""
    flag = False
    token_count = 1
    
    while 1:

        next_char = file.read(1)
        if flag:
            break

        if not next_char:
            next_char = ' '
            flag = True

        if next_char not in column:
            error_char = next_char
            next_char = ' '
            current_state = next_state
            next_state = DFA_array[current_state][find_index(next_char, column)]
            token_list.append(error_char)
            print("'", error_char, "'", "is not a valid input in alphabet")

        next_state = DFA_array[current_state][find_index(next_char, column)]
        token, token_type , tk_list, token_flag = find_tokens(next_state,current_state , char, token,flag)

        if token_flag:
            token_list.append(tk_list)
            token = res(token, token_type,token_count)

            token_count +=1

        char = next_char
        current_state = next_state

    file.close()'''


def lexer(program, DFA_array, column):
    current_state = 0
    file = open(program, 'r')
    token = ''
    char = ""
    flag = False
    token_count = 1
    line_count = 2

    while 1:

        next_char = file.read(1)
        if flag:
            break

        if not next_char:
            next_char = ' '
            flag = True

        if next_char not in column:
            error_char = next_char
            next_char = ' '
            current_state = next_state
            next_state = DFA_array[current_state][find_index(next_char, column)]
            token_list.append(error_char)
            print("'", error_char, "'", "is not a valid input in alphabet")

        next_state = DFA_array[current_state][find_index(next_char, column)]
        token, token_type, tk_list, token_flag = find_tokens(next_state, current_state, char, token, flag)

        if token_flag:
            token_list.append(tk_list)
            token = res(token, token_type, token_count)
            if next_char == '\n':
                print("\nline : " ,line_count,)
                line_count += 1
#            token = res(token, token_type, token_count)

            token_count += 1

        char = next_char
        current_state = next_state

    file.close()


def find_tokens(next_state, current_state, char, token,flag):
    if char != '\n':
        token += char
    token_flag = False
    token_type= ''

    if (next_state == 0).any() or flag:

        # condition 1 : "identifier"
        if (current_state == 1).any():
            token_type = "identifier"
            token_flag = True
            #token = res(token, token_type)

        # condition 3 : "digit"
        elif (current_state == 8).any():
            token_type = "number"
            token_flag = True
            #token = res(token, token_type)

        # condition 4 : "operator"
        elif (current_state == 9).any() or (current_state == 10).any() or (current_state == 11).any() or (current_state == 12).any():
            token_type = "operator"
            token_flag = True
            #token = res(token, token_type)

        # condition 5 : "punctuation"
        elif (current_state == 13).any() :
            token_type = "punctuation"
            token_flag = True
            #token = res(token, token_type)

        # condition 2 : "keyword"
        elif (current_state == 3).any() or (current_state == 7).any():
            token_type = "keyword"
            token_flag = True
            #token = res(token, token_type)

        elif (current_state == 14).any():
            
            token_type = "trap"
            token_flag = True
            print(" \nerror in this token -------")
            token = res(token, token_type)
            print("---------------------------\n")

    return token, token_type, (token,token_type), token_flag


def res(token, token_type, token_count):
    print(token_count ,") " ,token , ",", token_type)
    token = ""
    return token


print("line : 1\n")
dfa_array, column = read_csv_file(csv_path)
#count(program_path)
lexer(program_path, dfa_array, column)
print("\n" ,token_list)

