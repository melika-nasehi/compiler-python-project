symbol_table_semantic = []


# parser result --> ast (phase 3)
def semantic(parser_result):
    semantic_analyze(parser_result)

def semantic_analyze(ast):
    if isinstance(ast, tuple) and len(ast) > 0:
        if ast[0] == 'var_decl' :
            create_symbol_table(ast)

        if ast[0] == 'assign_stmt':
            check_assignment_type_match(ast)


        for item in ast:
            semantic_analyze(item)

def create_symbol_table(ast) :
    symbol_table_semantic.append({
        "type": ast[2][1],
        "id": ast[1],
        "value": None
    })


def check_assignment_type_match(ast):

    if ast[1][0] == 'location' :
        left_is_defined, left_type = check_defind(ast[1][1])

        if ast[2][1][0] == 'location' :
            right_is_defined, right_type = check_defind(ast[2][1][1])

            if not left_is_defined:
                print(f"ERROR: variable {ast[1][1]} is not defined !")
            if not right_is_defined:
                print(f"ERROR: variable {ast[2][1][1]} is not defined !")

            if right_type != left_type :
                print(f"ERROR: {ast[1][1]} and {ast[2][1][1]} dont have same type")

        elif ast[2][1][0] == 'int_literal' :
            if left_type != "int" :
                print(f"ERROR: {ast[1][1]} is not integer")

        elif ast[2][1][0] == 'bool_literal':
            if left_type != "boolean":
                print(f"ERROR: {ast[1][1]} is not boolean")

        elif ast[2][1][0] == 'char':
            if left_type != "char_literal" :
                print(f"ERROR: {ast[1][1]} is not char")


def check_defind(ast):
    found = False
    for item in symbol_table_semantic :
        if ast == item["id"] :
            return True , item["type"]
    if not found:
        return False , None