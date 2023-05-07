from Lexer import Lexer
from Parser import Parser

text_input = """
Brilha Brilha Estrelinha;

tempo = 120;

C jônio

4/4

&G C3:4 C3:4 G3:4 G3:4 ; A3:4 A3:4 G3:4 Z:4 ; F3:4 F3:4 E3:4 E3:4 ;
||: D3:16 Z:8 C3:16 D3:16 Z:8 E3:16 C3:2 :|| ; Z:1 ||
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()