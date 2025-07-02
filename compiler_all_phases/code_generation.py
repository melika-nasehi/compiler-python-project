from semantic import *

class CodeGeneration:
    semantic_stack = {}
    stack_pointer = 0
    address_dictionary = {}
    address = 1000



def code_generate(ast):
    cg = CodeGeneration
    add_to_dictionary(ast)
    generate(ast)
    print("memory")
    print(cg.address_dictionary)
    print("semantic stack")
    print(cg.semantic_stack)


def generate(ast):
    left_exp = ''
    right_exp = ''
    operator = ''
    if isinstance(ast, tuple) and len(ast) > 0:
        if ast[0] == 'assign_stmt':
            pid(ast[1][1] , False )
            if ast[1][0] == 'location':
                left_exp = ast[1][1]
            if ast[2][0] == 'exp' :
                right_exp = ast[2][1][1]
            if ast[2][0] == 'binary_op':
                operator = ast[2][1]
                generate(ast[2][0])
            #print(ast[2])
            assign(left_exp , right_exp , operator)

        if ast[0] == 'exp':
            int_flag = False
            if ast[1][0] == 'int_literal':
                int_flag = True
            pid(ast[1][1]  ,int_flag)


        if ast[0] == 'while_stmt' :
            print(ast)
            int_flag = False
            if ast[1] == 'binary_op' :
                if ast[1][2] == 'exp':
                    if ast[1][2][1][0] == 'int_literal' :
                        int_flag = True
                    pid(ast[1][2][1][1] , int_flag)
        for item in ast:
            generate(item)



def add_to_dictionary(ast):
    if isinstance(ast, tuple) and len(ast) > 0:
        if ast[0] == 'var_decl' :
            # id --> ast[1]
            cg = CodeGeneration
            cg.address_dictionary[ast[1]] = cg.address
            cg.address +=1
        for item in ast:
            add_to_dictionary(item)


def pid(input , int_flag):
    addr = find_address(input , int_flag)
    push(addr)


def find_address(input, int_flag):
    cg = CodeGeneration
    if int_flag :
        address = input
    else :
        address = cg.address_dictionary.get(input)
    return address


def push(addr):
    cg = CodeGeneration
    cg.semantic_stack[cg.stack_pointer] = addr
    cg.stack_pointer +=1


def assign(left_exp , right_exp, operator):
    print (f"{left_exp ,operator, right_exp}")

