from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def add_tokens(self):
        self.lexer.add('FRAC', '-?\d+.\d+')
        self.lexer.add('WHOLE', '-?\d+')
        self.lexer.add('WORD', '(""".?""")|(".?")|(\'.?\')')
        self.lexer.add('BOOL', 'true(?!\w)|false(?!\w)')

        self.lexer.add('K_WHOLE', 'whole(?!\w)')
        self.lexer.add('K_FRAC', 'frac(?!\w)')
        self.lexer.add('K_WORD', 'word(?!\w)')
        self.lexer.add('K_BOOL', 'bool(?!\w)')
        self.lexer.add('K_LETTER', 'letter(?!\w)')

        self.lexer.add('IF', 'if(?!\w)')
        self.lexer.add('OTHER', 'other(?!\w)')
        self.lexer.add('OTIF', 'otif(?!\w)')

        self.lexer.add('LOOP', 'loop(?!\w)')
        self.lexer.add('LOOPTILL', 'looptill(?!\w)')
        self.lexer.add('ENDNOW', 'endnow(?!\w)')
        self.lexer.add('RESUME', 'resume(?!\w)')


        self.lexer.add('AND', 'and(?!\w)')
        self.lexer.add('OR', 'or(?!\w)')
        self.lexer.add('NOT', 'not(?!\w)')

        self.lexer.add('FUNCTION', 'func(?!\w)')
        self.lexer.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]")
        self.lexer.add('EQUAL', '\==')
        self.lexer.add('NOT_EQUAL', '\!=')
        self.lexer.add('GREATER_EQUAL', '\>=')
        self.lexer.add('LESS_EQUAL', '\<=')
        self.lexer.add('GREATER_THAN', '\>')
        self.lexer.add('LESS_THAN', '\<')
        self.lexer.add('ASSIGNMENT', '\=')
        self.lexer.add('LEFT_BRACKET', '\[')
        self.lexer.add('RIGHT_BRACKET', '\]')
        self.lexer.add('LEFT_PARAN', '\{')
        self.lexer.add('RIGHT_PARAN', '\}')
        self.lexer.add('COMMA', '\,')
        self.lexer.add('DOT', '\.')
        self.lexer.add('COLON', '\:')
        self.lexer.add('PLUS', '\+')
        self.lexer.add('MINUS', '\-')
        self.lexer.add('MUL', '\*')
        self.lexer.add('DIV', '\/')
        self.lexer.add('MOD', '\%')
        self.lexer.add('RIGHT_BRACES', '\(')
        self.lexer.add('LEFT_BRACES', '\)')
        self.lexer.add('NEWLINE', '\n')

        # ignore whitespace
        self.lexer.ignore('[ \t\r\f\v]+')

    def get_lexer(self):
        self.add_tokens()
        return self.lexer.build()

lexer = Lexer().get_lexer()
print(lexer.lex("abc").next().gettokentype())