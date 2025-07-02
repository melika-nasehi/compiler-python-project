import pandas as pan
import numpy as np
from numpy.ma.core import array

csv_path = "DFAtoTable_Compiler.csv"
global token
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
c_program_path = "program.txt"

def read(file_path) :
    with open(file_path , 'r') as file :
        for line in file :
            for char in line :
                return char

def find_index(input_char, column):
    for i, char in enumerate(column):
        if char==input_char:
            return i


"""
def lexer(program , DFA_array, column):
    current_state = 0
    token_list = []
    with open(program , 'r') as file :
        for line in file :
            for char in line :
                if char is None:
                    break
                current_state = DFA_array[current_state][find_index(char, column)]
                #find_tokens(current_state, char)
                print(current_state)
                """

def lexer(program , DFA_array, column):
    current_state = 0
    token_list = []
    file = open(program, 'r')
    token = ''
    while 1:
        char = file.read(1)
        if not char:
            break
        current_state = DFA_array[current_state][find_index(char, column)]
        token , tuplee, flag = find_tokens(current_state, char, token)
        if flag :
            token_list.append(tuplee)
            token = ''
    file.close()
    return token_list

        #print(current_state)


def find_tokens(current_state, char, token):
    token += char
    #next_state =
    # condition 1 : "identifier"
    if (current_state == 2).any() :
        token_type = "identifier"
        return token, (token, token_type) , True


    # condition 2 : "keyword"
    elif current_state == 11:
        token_type = "keyword"
        return token , (token, token_type), True


    # condition 3 : "digit"
    elif current_state == 4:
        token_type = "number"
        return token ,(token, token_type), True



    # condition 4 : "operator"
    elif current_state == 12:
        token_type = "operator"
        return token , (token, token_type), True


    # condition 5 : "punctuation"
    elif current_state == 13:
        token_type = "punctuation"
        return token ,(token, token_type), True

    else :
        return token , (), False


def res(token, token_type):
    print(token , ",", token_type)
    token = ""
    return token


dfa_array, column = read_csv_file(csv_path)
print(lexer(program_path, dfa_array, column))