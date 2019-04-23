from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lg = LexerGenerator()

    def add_tokens(self):
        self.lg.add('FRAC', '-?\d+.\d+')
        self.lg.add('WHOLE', '-?\d+')
        self.lg.add('WORD', '(""".?""")|(".?")|(\'.?\')')
        self.lg.add('BOOL', 'true(?!\w)|false(?!\w)')

        self.lg.add('K_WHOLE', 'whole(?!\w)')
        self.lg.add('K_FRAC', 'frac(?!\w)')
        self.lg.add('K_WORD', 'word(?!\w)')
        self.lg.add('K_BOOL', 'bool(?!\w)')
        self.lg.add('K_LETTER', 'letter(?!\w)')

        self.lg.add('IF', 'if(?!\w)')
        self.lg.add('OTHER', 'other(?!\w)')
        self.lg.add('OTIF', 'otif(?!\w)')

        self.lg.add('LOOP', 'loop(?!\w)')
        self.lg.add('LOOPTILL', 'looptill(?!\w)')
        self.lg.add('ENDNOW', 'endnow(?!\w)')
        self.lg.add('RESUME', 'resume(?!\w)')


        self.lg.add('AND', 'and(?!\w)')
        self.lg.add('OR', 'or(?!\w)')
        self.lg.add('NOT', 'not(?!\w)')

        self.lg.add('FUNCTION', 'func(?!\w)')
        self.lg.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]+")
        self.lg.add('EQUAL', '\==')
        self.lg.add('NOT_EQUAL', '\!=')
        self.lg.add('GREATER_EQUAL', '\>=')
        self.lg.add('LESS_EQUAL', '\<=')
        self.lg.add('GREATER_THAN', '\>')
        self.lg.add('LESS_THAN', '\<')
        self.lg.add('ASSIGNMENT', '\=')
        self.lg.add('LEFT_BRACKET', '\[')
        self.lg.add('RIGHT_BRACKET', '\]')
        self.lg.add('LEFT_PARAN', '\{')
        self.lg.add('RIGHT_PARAN', '\}')
        self.lg.add('COMMA', '\,')
        self.lg.add('DOT', '\.')
        self.lg.add('COLON', '\:')
        self.lg.add('PLUS', '\+')
        self.lg.add('MINUS', '\-')
        self.lg.add('MUL', '\*')
        self.lg.add('DIV', '\/')
        self.lg.add('MOD', '\%')
        self.lg.add('RIGHT_BRACES', '\(')
        self.lg.add('LEFT_BRACES', '\)')
        self.lg.add('NEWLINE', '\n')

        # ignore whitespace
        self.lg.ignore('[ \t\r\f\v]+')

    def get_lexer(self):
        self.add_tokens()
        return self.lg.build()

lexer = Lexer().get_lexer()
for token in lexer.lex('abccc'):
    print(token)