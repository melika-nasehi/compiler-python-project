
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

def p_Program(p):
    '''Program : CLASS PROGRAM LBRACE FieldDecls MethodDecls RBRACE'''
    p[0] = ('Program', p[4], p[5])

def p_FieldDecls(p):
    '''FieldDecls : FieldDecl FieldDecls
                   | empty'''
    if len(p) == 3:
        p[0] = ((p[1]), p[2])
    else:
        p[0] = ()

def p_FieldDecl(p):
    '''FieldDecl : Type IDENTIFIER SEMICOLON
                  | Type IDENTIFIER LBRACKET IntLiteral RBRACKET SEMICOLON'''
    if len(p) == 4:
        p[0] = ('field_decl', p[1], p[2])
    else:
        p[0] = ('filed_constant', p[1], p[2], p[4])

def p_MethodDecls(p):
    '''MethodDecls : MethodDecl MethodDecls
                    | empty'''
    if len(p) == 3:
        p[0] = ((p[1]), p[2])
    else:
        p[0] = ()

def p_MethodDecl(p):
    '''MethodDecl : Type IDENTIFIER LPAREN ParamList RPAREN Block
                   | VOID IDENTIFIER LPAREN RPAREN Block'''
    if len(p) == 6:
        p[0] = ('method_declare1', p[1], p[2], [], p[5])
    else:
        p[0] = ('method_declare2', p[1], p[2], p[4], p[5])

def p_ParamList(p):
    '''ParamList : Type IDENTIFIER
                  | Type IDENTIFIER COMMA ParamList'''
    if len(p) == 3:
        p[0] = ('param', p[1], p[2])
    else:
        p[0] = ('param', p[1], p[2], p[4])

def p_Block(p):
    '''Block : LBRACE VarDecls Statements RBRACE'''
    p[0] = ('block', p[2], p[3])

def p_VarDecls(p):
    '''VarDecls : VarDecl VarDecls
                 | empty'''
    if len(p) == 3:
        p[0] = ('ssssss', p[1], p[2])
    else:
        p[0] = ()

def p_VarDecl(p):
    '''VarDecl : Type IDENTIFIER SEMICOLON'''
    p[0] = ('var_decl', p[2], p[1])

def p_type(p):
    '''Type : INT
             | BOOLEAN'''
    p[0] = ('type_declare', p[1])

def p_Statements(p):
    '''Statements : Statement Statements
                  | empty'''
    if len(p) == 3:
        p[0] = (p[1], p[2])
    else:
        p[0] = ()

def p_Statement(p):
    '''Statement : Location ASSIGN Expression SEMICOLON
                  | MethodCall SEMICOLON
                  | IF LPAREN Expression RPAREN Block
                  | IF LPAREN Expression RPAREN Block ELSE Block
                  | WHILE LPAREN Expression RPAREN Block
                  | RETURN Expression SEMICOLON
                  | RETURN SEMICOLON
                  | BREAK SEMICOLON
                  | CONTINUE SEMICOLON
                  | Block'''
    if len(p) == 2:
        p[0] = ('block_stmt', p[1])
    elif len(p) == 5 and p[2] == '=':
        p[0] = ('assign_stmt', p[1], p[3])
    elif len(p) == 6 and p[1] == 'if':
        p[0] = ('if_stmt', p[3], p[5])
    elif len(p) == 8:
        p[0] = ('if_else_stmt', p[3], p[5], p[7])
    elif len(p) == 6 and p[1] == 'while':
        p[0] = ('while_stmt', p[3], p[5])
    elif len(p) == 4:
        p[0] = ('return_stmt', p[2])
    elif len(p) == 3:
        if p[1] == 'break':
            p[0] = ('break_stmt',)
        elif p[1] == 'continue':
            p[0] = ('continue_stmt',)
        elif p[1] == 'return':
            p[0] = ('return_stmt',)
        else:
            p[0] = ('method_call', p[1])

def p_MethodCall(p):
    '''MethodCall : IDENTIFIER LPAREN RPAREN
                   | IDENTIFIER LPAREN ExpressionList RPAREN
                   | CALLOUT LPAREN StringLiteral RPAREN
                   | CALLOUT LPAREN StringLiteral COMMA CalloutArgList RPAREN'''
    if len(p) == 4:
        p[0] = ('method()', p[1])
    elif len(p) == 5 and p[1] == 'callout':
        p[0] = ('meyhod(expr_list)', p[1], p[3])
    elif len(p) == 6:
        p[0] = ('callout(str, args, ...)', p[3], p[5])
    else:
        p[0] = ('callout(str)', p[3])

def p_Location(p):
    '''Location : IDENTIFIER
                | IDENTIFIER LBRACKET Expression RBRACKET'''
    if len(p) == 2:
        p[0] = ('location', p[1])
    else:
        p[0] = ('id [expr]', p[1], p[3])

def p_ExpressionList(p):
    '''ExpressionList : Expression
                       | Expression COMMA ExpressionList'''
    if len(p) == 2:
        p[0] = ('expression', p[1])
    else:
        p[0] = ('expression_list', p[1], p[3])

def p_Expression(p):
    '''Expression : Location
                  | MethodCall
                  | Literal
                  | Expression BinOp Expression
                  | MINUS Expression
                  | NOT Expression
                  | LPAREN Expression RPAREN'''
    if len(p) == 2:
        p[0] = ('exp', p[1])
    elif len(p) == 4:
        if p[1] == '(':
            p[0] = p[2]
        else:
            p[0] = ('binary_op', p[2], p[1], p[3])
    else:
        p[0] = p[2]

def p_CalloutArgList(p):
    '''CalloutArgList : CalloutArg
                       | CalloutArg COMMA CalloutArgList'''
    if len(p) == 2:
        p[0] = ('single_arg', p[1])
    else:
        p[0] = ('multi_args', p[1], p[3])

def p_CalloutArg(p):
    '''CalloutArg : Expression
                   | StringLiteral'''
    p[0] = p[1]

def p_BinOp(p):
    '''BinOp : ArithOp
              | RelOp
              | EqOp
              | CondOp'''
    p[0] = p[1]

def p_ArithOp(p):
    '''ArithOp : PLUS
                | MINUS
                | MULTIPLY
                | DIVIDE
                | MODULO
                | SHIFT_L
                | SHIFT_R
                | LSHIFT_R'''
    p[0] = p[1]

def p_RelOp(p):
    '''RelOp : GREATER
              | LESS
              | GREATER_EQUAL
              | LESS_EQUAL'''
    p[0] = p[1]

def p_EqOp(p):
    '''EqOp : EQUAL
             | NOT_EQUAL'''
    p[0] = p[1]

def p_CondOp(p):
    '''CondOp : LOGICAL_AND
               | LOGICAL_OR'''
    p[0] = p[1]

def p_Literal(p):
    '''Literal : IntLiteral
                | CharLiteral
                | BoolLiteral'''
    p[0] = p[1]

def p_IntLiteral(p):
    '''IntLiteral : DecimalLiteral
                   | HexLiteral'''
    p[0] = ('int_literal', p[1])

def p_DecimalLiteral(p):
    '''DecimalLiteral : NUMBER'''
    p[0] = p[1]

def p_HexLiteral(p):
    '''HexLiteral : HEX_NUMBER'''
    p[0] = p[1]

def p_BoolLiteral(p):
    '''BoolLiteral : TRUE
                    | FALSE'''
    p[0] = ('bool_literal', p[1])

def p_CharLiteral(p):
    '''CharLiteral : CHAR_LITERAL'''
    p[0] = ('char', p[1])

def p_StringLiteral(p):
    '''StringLiteral : STRING_LITERAL'''
    p[0] = p[1]

def p_empty(p):
    '''empty : '''
    pass

# Error handling function
def p_error(p):
    print("Syntax error at token:", p)