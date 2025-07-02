from dataclasses import fields

import pandas as pan
import numpy as np
from numpy.ma.core import array

csv_path = "DFAtoTable_Compiler.csv"

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

# adding the alphabet column 
def find_index(input_char, column):
    for i, char in enumerate(column):
        if char==input_char:
            return i

def lexer(program , DFA_array, column):
    current_state = 0
    file = open(program, 'r')
    token = ''
    char = ""
    flag = False

    while 1:

        next_char = file.read(1)
        if flag:
            break

        if not next_char:
            next_char = ' '
            flag = True


        invalid_input = False
        try:
            next_state = DFA_array[current_state][find_index(next_char, column)]
        except :
            print("'", char,"'", "is not a valid input in alphabet")
            invalid_input = True

        if not invalid_input:
            token = find_tokens(next_state,current_state , char, token,flag)

        #print(char, "       ", next_char)

        char = next_char
        #print(current_state , "      ", next_state)
        current_state = next_state
        #print(next_char)
        #print(char)
    file.close()


def find_tokens(next_state, current_state, char, token,flag):
    token += char
    token_flag = False
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
           # token = res(token, token_type)

        # condition 4 : "operator"
        elif (current_state == 9).any():
            token_type = "operator"
            token_flag = True
            #token = res(token, token_type)

        # condition 5 : "punctuation"
        elif (current_state == 10).any() or (current_state == 11).any():
            token_type = "punctuation"
            token_flag = True
            #token = res(token, token_type)

        # condition 2 : "keyword"
        elif (current_state == 3).any():
            token_type = "keyword"
            token_flag = True
            #token = res(token, token_type)

        elif (current_state == 12).any():
            token_type = "trap"
            token_flag = True
            print(" \nerror in this token -------")
            #token = res(token, token_type)
            print("---------------------------")

    return token, token_type, token_flag


def res(token, token_type):
    print(token , ",", token_type)
    token = ""
    return token



dfa_array, column = read_csv_file(csv_path)
lexer(program_path, dfa_array, column)