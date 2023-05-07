from rply import ParserGenerator
from ast import Musica


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['ANDAMENTO', 'DIVISAO_METRICA', 'DURACAO', 'TITULO', 'PAUSA',
             'LOOP_START', 'LOOP_END', 'FIM_DA_MUSICA', 'CLAVE', 'CONDITIONAL',
             'ALTURA', 'LETTER', 'FIM_COMPASSO', 'TO_DUR']
        )

    def parse(self):
        @self.pg.production("musica : TITULO ANDAMENTO LETTER CONDITIONAL DIVISAO_METRICA compassos FIM_DA_MUSICA")
        def musica(p):
            # Handle the production logic here
            # p[0] corresponds to TITULO, p[1] to ANDAMENTO, p[2] to ESCALA, and so on.
            return Musica(p[1], p[3], p[4])
            

        @self.pg.production("compassos : compasso compassos")
        def compassos(p):
            # Handle the production logic here
            # p[0] corresponds to compasso, p[1] to compassos
            pass

        @self.pg.production("compasso : CLAVE notas FIM_COMPASSO")
        def compasso(p):
            # Handle the production logic here for an empty list of compassos
            pass

        @self.pg.production("notas : ALTURA TO_DUR DURACAO notas")
        def notas(p):

            pass
    
        @self.pg.production("notas : PAUSA DURACAO notas")
        def pausas(p):

            pass

        @self.pg.production("loop : LOOP_START compassos LOOP_END")
        def loop(p):

            pass

        @self.pg.error
        def error_handle(token):
            raise ValueError("Error parsing input. Unexpected token '{}'".format(token.gettokentype()))


    def get_parser(self):
        return self.pg.build()