import ply.yacc as yacc
from Phase2 import tokens
from semantic import *

precedence = (
    ('right', 'ASSIGN'),
    ('left', 'LOGICAL_OR'),
    ('left', 'LOGICAL_AND'),
    ('left', 'EQUAL', 'NOT_EQUAL'),
    ('left', 'LESS_EQUAL', 'GREATER_EQUAL', 'LESS', 'GREATER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'NOT'),
)
def p_start(p):
    '''start : program'''
    p[0] = ('start' , p[1])
    pass
def p_program(p):
    '''program : CLASS IDENTIFIER LEFT_BRACE field_decl_list RIGHT_BRACE
                | CLASS IDENTIFIER LEFT_BRACE method_decl_list RIGHT_BRACE'''
    p[0] = ('program' , p[1] , p[2] , p[3] , p[4] , p[5] )
    pass

def p_field_decl_list(p):
    '''field_decl_list : field_decl field_decl_list
    | lambda'''
    if len(p) == 3:
        p[0] = ('field_decl_list',p[1],p[2])
    elif len(p) == 2:
        p[0] = ('field_decl_list', p[1])
    pass
def p_field_decl (p):
    '''field_decl : type IDENTIFIER COMMA SEMICOLON
    | type IDENTIFIER LEFT_BRACKET int_literal RIGHT_BRACKET COMMA SEMICOLON'''
    if len(p) == 5:
        p[0] = ('field_decl',p[1],p[2],p[3],p[4])
    elif len(p) == 8:
        p[0] = ('field_decl', p[1],p[2],p[3],p[4],p[5],p[6],p[7])
    pass

def p_method_decl_list(p):
    '''method_decl_list : method_decl method_decl_list
    | lambda'''
    if len(p) == 3:
        p[0] = ('method_decl_list',p[1],p[2])
    elif len(p) == 2:
        p[0] = ('method_decl_list', p[1])
    pass


def p_method_decl(p):
    '''method_decl : type IDENTIFIER LEFT_PAREN method_input_list RIGHT_PAREN block
                    | VOID IDENTIFIER LEFT_PAREN method_input_list RIGHT_PAREN block'''
    p[0] = ('method_decl' , p[1] , p[2] , p[3] , p[4], p[5], p[6])
    pass

def p_method_input_list(p):
    '''method_input_list : method_input method_input_list
    | lambda'''
    if len(p) == 3:
        p[0] = ('method_decl_list',p[1],p[2])
    elif len(p) == 2:
        p[0] = ('method_decl_list', p[1])
    pass

def p_method_input(p):
    '''method_input : type IDENTIFIER COMMA'''
    p[0] = ('method_input' , p[1],p[2],p[3])
    pass

def p_block(p):
    '''block : LEFT_BRACE p_block_content_list RIGHT_BRACE'''
    p[0] = ('block', p[1], p[2], p[3])
    pass

def p_block_content_list(p):
    '''p_block_content_list : statement_list p_block_content_list
                            | var_decl_list p_block_content_list
                            | lambda'''
    if len(p) == 3:
        p[0] = ('p_block_content_list',p[1],p[2])
    elif len(p) == 2:
        p[0] = ('p_block_content_list', p[1])
    pass

def p_var_decl_list(p):
    '''var_decl_list : var_decl var_decl_list
    | lambda'''
    if len(p) == 3:
        p[0] = ('var_decl_list',p[1],p[2])
    elif len(p) == 2:
        p[0] = ('var_decl_list', p[1])
    pass

def p_var_decl(p):
    '''var_decl : type IDENTIFIER COMMA var_id_list SEMICOLON'''
    p[0] = ('var_decl', p[1], p[2],p[3],p[4])
    pass

def p_var_id_list(p):
    '''var_id_list : IDENTIFIER COMMA var_id_list
    | lambda'''
    if len(p) == 4:
        p[0] = ('var_decl_list',p[1],p[2],p[3])
    elif len(p) == 2:
        p[0] = ('var_decl_list', p[1])
    pass

def p_type(p):
    '''type : BOOLEAN
    | INT'''
    p[0] = ('type', p[1])
    pass

def p_statement_list(p):
    '''statement_list : statement statement_list
    | lambda'''
    if len(p) == 3:
        p[0] = ('statement_list',p[1],p[2])
    elif len(p) == 2:
        p[0] = ('statement_list', p[1])
    pass

def p_statement(p):
    '''statement : location ASSIGN expr SEMICOLON
                    | method_call SEMICOLON
                    | IF LEFT_PAREN expr RIGHT_PAREN block else_section_question
                    | WHILE LEFT_PAREN expr RIGHT_PAREN block
                    | RETURN expr_question SEMICOLON
                    | BREAK SEMICOLON
                    | CONTINUE SEMICOLON
                    | block'''

    if len(p) == 5:
        p[0] = ('statement',p[1],p[2], p[3], p[4])
    elif len(p) == 3:
        p[0] = ('statement', p[1],p[2])
    elif len(p) == 7:
        p[0] = ('statement', p[1],p[2], p[3], p[4],p[5],p[6])
    elif len(p) == 4:
        p[0] = ('statement', p[1],p[2],p[3])
    elif len(p) == 2:
        p[0] = ('statement', p[1])
    elif len(p) == 6:
        p[0] = ('statement', p[1],p[2], p[3], p[4],p[5])
    pass

def p_else_section_question(p):
    '''else_section_question : ELSE block
    | lambda'''
    if len(p) == 3:
        p[0] = ('else_section_question',p[1],p[2])
    elif len(p) == 2:
        p[0] = ('else_section_question', p[1])
    pass

def p_expr_question(p):
    '''expr_question : expr
    | lambda'''
    p[0] = ('expr_question', p[1])
    pass

def p_method_call(p):
    '''method_call : method_name LEFT_PAREN method_call_values RIGHT_PAREN
                    | CALLOUT LEFT_PAREN string_literal callout_arg_question RIGHT_PAREN'''
    if len(p) == 5:
        p[0] = ('method_call', p[1], p[2], p[3], p[4])
    elif len(p) ==6:
        p[0] = ('method_call', p[1], p[2], p[3], p[4],p[5])
    pass

def p_callout_arg_question(p):
    '''callout_arg_question : callout_arg_list
    | lambda'''
    p[0] = ('callout_arg_question', p[1])
    pass

def p_callout_arg_list(p):
    '''callout_arg_list : callout_arg COMMA callout_arg_list
    | callout_arg COMMA'''
    if len(p) == 4:
        p[0] = ('method_call', p[1], p[2], p[3])
    elif len(p) ==3:
        p[0] = ('method_call', p[1], p[2])
    pass

def p_method_call_values(p):
    '''method_call_values : expr COMMA method_call_values
    | lambda'''
    if len(p) == 4:
        p[0] = ('method_call_values', p[1], p[2],p[3])
    elif len(p) == 2:
        p[0] = ('method_call_values', p[1])
    pass

def p_method_name(p):
    '''method_name : IDENTIFIER'''
    p[0] = ('method_name', p[1])
    pass

def p_location(p):
    '''location : IDENTIFIER
    | IDENTIFIER LEFT_BRACKET expr RIGHT_BRACKET'''
    if len(p) == 5:
        p[0] = ('location', p[1], p[2],p[3],p[4])
    elif len(p) == 2:
        p[0] = ('location', p[1])
    pass
def p_expr(p):
    '''expr : location
            | method_call
            | literal
            | expr bin_op expr
            | MINUS expr
            | NOT expr
            | LEFT_PAREN expr RIGHT_PAREN'''

    if len(p) == 4:
        p[0] = ('expr', p[1], p[2],p[3])
    elif len(p) == 3:
        p[0] = ('expr', p[1],p[2])
    elif len(p) == 2:
        p[0] = ('expr', p[1])
    pass

def p_callout_arg(p):
    '''callout_arg : expr
    | string_literal'''
    p[0] = ('callout_arg', p[1])
    pass
def p_bin_op(p):
    '''bin_op : arith_op
    | rel_op
    | eq_op
    | cond_op'''
    p[0] = ('bin_op', p[1])
    pass

def p_arith_op(p):
    '''arith_op : PLUS
    | MINUS
    | MULTIPLY
    | DIVIDE
    | MODULO
    | SHIFT_R_A
    | SHIFT_R_L
    | SHIFT_L'''
    p[0] = ('arith_op', p[1])
    pass

def p_rel_op(p):
    '''rel_op : GREATER
    | LESS
    | GREATER_EQUAL
    | LESS_EQUAL'''
    p[0] = ('rel_op', p[1])
    pass

def p_eq_op(p):
    '''eq_op : EQUAL
    | NOT_EQUAL'''
    p[0] = ('eq_op', p[1])
    pass

def p_cond_op(p):
    '''cond_op : AND
    | OR'''
    p[0] = ('cond_op', p[1])
    pass

def p_literal(p):
    '''literal : int_literal
    | char_literal
    | bool_literal'''
    p[0] = ('literal', p[1])
    pass

def p_int_literal(p):
    '''int_literal : NUMBER
        | HEX_NUMBER'''
    p[0] = ('int_literal', p[1])
    pass

def p_bool_literal(p):
    '''bool_literal : TRUE
        | FALSE'''
    p[0] = ('bool_literal', p[1])
    pass

def p_char_literal(p):
    '''char_literal : CHARACTER'''
    p[0] = ('char_literal', p[1])
    pass

def p_string_literal(p):
    '''string_literal : STRING'''
    p[0] = ('string_literal', p[1])
    pass

def p_error(error):
    print('syntax error: ', error)
    pass


def p_lambda(p):
    'lambda : '
    pass

# Build the parser
parser = yacc.yacc()
#ast = parser.parse()
#print(ast)

# Test the parser
filename = 'test.c'
with open(filename, 'r') as file:
    data = file.read()
    try:
        ast = parser.parse(data)
        print(ast)
    except Exception as e:
        print("Parser error:", e)
#print(ast[0])
init(ast)
print(symbol_table_semantic)