from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        
        # self.lexer.add("TITULO", r"[A-Za-z0-9][A-Za-z0-9\s]*;")
        # self.lexer.add("ANDAMENTO", r"tempo\s*=\s*\d+;")
        # self.lexer.add("DIVISAO_METRICA", r"\d/\d")
        # self.lexer.add("PAUSA", r"Z:\d")
        # self.lexer.add("LOOP_START", r"\|\|:")
        # self.lexer.add("LOOP_END", r":\|\|;")
        # self.lexer.add("FIM_DA_MUSICA", r"\|\|")
        # self.lexer.add("CLAVE", r"&[GF]")
        # self.lexer.add("NOTA", r"[#b]?[A-G][0-9]+:[0-9]+")
        # self.lexer.add("CONDITIONAL", r"[A-G] jônio|dórico|frígio|lídio|mixolídio|eólio|lócrio")
        # self.lexer.add("FIM_COMPASSO", r"\;")
        
        self.lexer.add("ANDAMENTO", r"tempo\s*=\s*\d+;")
        self.lexer.add("DIVISAO_METRICA", r"\d/\d")
        self.lexer.add("DURACAO", r"\d+")
        self.lexer.add("TITULO", r"[A-Za-z0-9][A-Za-z0-9\s]*;")
        self.lexer.add("PAUSA", r"Z")
        self.lexer.add("LOOP_START", r"\|\|:")
        self.lexer.add("LOOP_END", r":\|\|")
        self.lexer.add("FIM_DA_MUSICA", r"\|\|")
        self.lexer.add("CLAVE", r"&[GF]")
        self.lexer.add("CONDITIONAL", r"jônio|dórico|frígio|lídio|mixolídio|eólio|lócrio")
        self.lexer.add("ALTURA", r"[A|B|C|D|E|F|G]\d")
        self.lexer.add("FIM_COMPASSO", r"\;")
        self.lexer.add("TO_DUR", r":")
        self.lexer.add("MODULACAO", r"#|b")
        self.lexer.add("COND_ALTURA", r"[A-Z]")
        

        # Ignore white spaces
        self.lexer.ignore(r"\s+")

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()