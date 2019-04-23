from rply import ParserGenerator, LexerGenerator
from rply.token import BaseBox

lg = LexerGenerator()
# Add takes a rule name, and a regular expression that defines the rule.
lg.add("WHOLE", r"whole")
lg.add("FRAC", r"frac")
lg.add("WORD ", r"frac")
lg.add("LETTER", r"letter")
lg.add("BOOL", r"bool")
lg.add("IF", r"If")
lg.add("RESUME", r"resume")
lg.add("OTHER", r"other")
lg.add("OTIF", r"otif")
lg.add("LOOP", r"loop")
lg.add("ENDNOW", r"looptill")
lg.add("LOOPTILL", r"endnow")
lg.add("OPENBRAC", r"\(")
lg.add("CLOSEBRAC", r"\)")
lg.add("OPENCURLY", r"\{")
lg.add("CLOSECURLY", r"\}")
lg.add("OPENSQU", r"\[")
lg.add("CLOSESQU", r"\]")
lg.add("OPENANGLE", r"\<")
lg.add("CLOSEANGLE", r"\>")
lg.add("SINGLEQUOT", r"\'")
lg.add("DOUBlEQUOT", r"\"")
lg.add("SEMICOLON", r"\;")
lg.add("EQUAL", r"\=")
lg.add("PLUS", r"\+")

lg.add("MINUS", r"\-")
lg.add("MULT", r"\*")
lg.add("DIVIDE", r"\\")

lg.ignore(r"\s+")


lexer = lg.build()
#parser = pg.build()


print(lexer.lex(";").next().gettokentype())
