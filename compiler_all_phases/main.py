import ply.yacc as yacc
from Phase2 import tokens
from semantic import *
from grammers import *
from code_generation import *



# Build the parser
parser = yacc.yacc(debug=True,start='Program',method='SLR')

# Test the parser
filename = 'test.c'
with open(filename, 'r') as file:
    data = file.read()
    try:
        result = parser.parse(data)
        print("AST:")
        print(result)
        print()
    except Exception as e:
        print("Parser error:", e)

semantic(result)
print()
print("symbol table :")
print(symbol_table_semantic)
print()
print("code generation :")
code_generate(result)