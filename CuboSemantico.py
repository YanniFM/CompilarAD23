class CuboSemantico:
# El cubo semántico define las reglas de tipo para operaciones entre diferentes tipos de datos.
# Cada entrada del diccionario principal representa un tipo de operando izquierdo.
# Cada sub-diccionario representa el tipo del operando derecho con las operaciones correspondientes.      
    def __init__(self) -> None:
        self.cubo = {
            'int': {
                'int': {
                    '+': 'int',
                    '-': 'int',
                    '*': 'int',
                    '/': 'int',
                    '%': 'int',
                    '<': 'bool',
                    '>': 'bool',
                    '<=': 'bool',
                    '>=': 'bool',
                    '==': 'bool',
                    '<>': 'bool',
                    '&': 'error',
                    '|': 'error',
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '%': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    '<=': 'bool',
                    '>=': 'bool',
                    '==': 'bool',
                    '<>': 'bool',
                    '&': 'error',
                    '|': 'error',
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'string': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
            },
            'float': {
                'int': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '%': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    '<=': 'bool',
                    '>=': 'bool',
                    '==': 'bool',
                    '<>': 'bool',
                    '&': 'error',
                    '|': 'error',
                },
                'float': {
                    '+': 'float',
                    '-': 'float',
                    '*': 'float',
                    '/': 'float',
                    '%': 'float',
                    '<': 'bool',
                    '>': 'bool',
                    '<=': 'bool',
                    '>=': 'bool',
                    '==': 'bool',
                    '<>': 'bool',
                    '&': 'error',
                    '|': 'error',
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'string': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
            },
            'char': {
                'int': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'float': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'bool',
                    '<>': 'bool',
                    '&': 'error',
                    '|': 'error',
                },
                'string': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
            },
            'string': {
                'int': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'float': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'string': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'bool',
                    '<>': 'bool',
                    '&': 'error',
                    '|': 'error',
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
            },
            'bool': {
                'int': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'float': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'char': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'string': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'error',
                    '|': 'error',
                },
                'bool': {
                    '+': 'error',
                    '-': 'error',
                    '*': 'error',
                    '/': 'error',
                    '%': 'error',
                    '<': 'error',
                    '>': 'error',
                    '<=': 'error',
                    '>=': 'error',
                    '==': 'error',
                    '<>': 'error',
                    '&': 'bool',
                    '|': 'bool',
                },
            },
        }
