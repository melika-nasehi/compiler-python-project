import ply.lex as pl

# Keywords
keywords = {
    "class": "CLASS",
    "int": "INT",
    "boolean": "BOOLEAN",
    "void": "VOID",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "return": "RETURN",
    "break": "BREAK",
    "continue": "CONTINUE",
    "true": "TRUE",
    "false": "FALSE",

    "program" : "PROGRAM",
    "callout" : "CALLOUT",
    "start": "START",

}


# Tokens
tokens = [
    "IDENTIFIER",
    "NUMBER",
    "HEX_NUMBER",
    "STRING_LITERAL",
    "CHAR_LITERAL",
    #"INVALID",

    "LBRACE",  # Left brace
    "RBRACE",  # Right brace
    "LPAREN",  # Left parenthesis
    "RPAREN",  # Right parenthesis
    "LBRACKET",  # Left bracket
    "RBRACKET",  # Right bracket
    "COMMA",
    "SEMICOLON",
    "ASSIGN",  # Assignment operator

    #"ARITH_OP",  # Arithmetic operator (+, -, *, /, %)
    "PLUS",
    "MINUS",
    "MULTIPLY",
    "DIVIDE",
    "MODULO",
    "SHIFT_L",
    "SHIFT_R",
    "LSHIFT_R",

    #REP_OP = r'[< | > | <= | >=]'
    "GREATER",
    "LESS",
    "GREATER_EQUAL",
    "LESS_EQUAL",

    #EQ_OP = r'==|!= | !'
    "EQUAL",
    "NOT_EQUAL",
    "NOT",

    #COND_OP = r'&&|\|\|'
    "LOGICAL_AND",
    "LOGICAL_OR"
]+ list(keywords.values())




#REGULAR EXPRESSIONS

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_ignore = ' \n\t'

#t_ARITH_OP = r'[ + | - | * | / | % | << | >> | >>>]'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_SHIFT_L = r'<<'
t_SHIFT_R = r'>>'
LSHIFT_R = r'>>>'

#t_REP_OP = r'[< | > | <= | >=]'
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='

#t_EQ_OP = r'==|!= | !'
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_NOT = r'!'

#t_COND_OP = r'&&|\|\|'
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'

def t_HEX_NUMBER(t):
    r'0x[0-9a-fA-F]+'
    return t

def t_INVALID(t):
    r'[0-9]+[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_.][a-zA-Z0-9_.]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_LITERAL(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CHAR_LITERAL(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print("INVALID TOKEN",t.value[0])
    t.lexer.skip(1)
    return t



lexer = pl.lex()

def read(path):
    with open(path,'r') as file :
        return file.read().rstrip()

program_string = read('test.c')

lexer.input(program_string)

while True:
    token = pl.token()
    if not token :
        break

    """print('< type :"',token.type, '" ,'
            ' value :"' , token.value ,'" ,'
            ' line number:' , lexer.lineno, ','
            ' token pos:' ,token.lexpos ,'>\n' )"""


