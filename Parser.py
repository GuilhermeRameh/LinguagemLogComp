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
        @self.pg.production("musica : TITULO ANDAMENTO LETTER CONDITIONAL DIVISAO_METRICA CLAVE compassos FIM_DA_MUSICA")
        def musica(p):
            print(p)
            pass
            

        @self.pg.production("compassos : compasso compassos")
        def compassos(p):
            print(p)
            pass

        @self.pg.production("compasso : notas FIM_COMPASSO")
        def compasso(p):
            print(p)
            pass

        @self.pg.production("notas : ALTURA TO_DUR DURACAO notas")
        def notas(p):
            print(p)
            pass
    
        @self.pg.production("notas : PAUSA TO_DUR DURACAO notas")
        def pausas(p):
            print(p)
            pass

        @self.pg.production("loop : LOOP_START compassos LOOP_END")
        def loop(p):
            print(p)
            pass

        @self.pg.error
        def error_handle(token):
            raise ValueError("Error parsing input. Unexpected token '{}'".format(token))


    def get_parser(self):
        return self.pg.build()