from Lexer import Lexer
from Parser import Parser

###################### NODES ######################
class Node():
    def Evaluate(self, ST):
        pass

class Musica(Node):
    def __init__(self, children) -> None:
        self.children = children

    def Evaluate(self):
        for child in self.children:
            child.Evaluate()

class Compasso(Node):
    def __init__(self, children) -> None:
        self.children = children

    def Evaluate(self):
        for child in self.children:
            child.Evaluate()

class Loop(Node):
    def __init__(self, children) -> None:
        self.children = children

    def Evaluate(self):
        for i in range(2):
            for child in self.children:
                child.Evaluate()


class Nota(Node):
    def __init__(self, children) -> None:
        self.children = children

    def Evaluate(self):
        if self.children[1]=="b": mod="Bemol" 
        else: mod="Sustenido" 
        if self.children[1] != "":
            print( self.children[0] + " " + mod + " " + "1/"+self.children[2])
        else:
            print( self.children[0] + " " + "1/"+self.children[2])

class NoOp(Node):
    def Evaluate(self):
        pass


##################### TOKENIZER ######################
class Tokenizer:
    def __init__(self, tokens) -> None:
        self.id = -1
        self.tokens = tokens
        self.next = tokens[0]
        self.selectNext()

    def selectNext(self):
        if self.id+1 == len(self.tokens):
            return
        self.id += 1
        self.next = self.tokens[self.id]


################### PARSER ###################
class Parser:
    def __init__(self):
        self.tokenizer = Tokenizer

    def parseNote(self):
        mod = ""
        if self.tokenizer.next.gettokentype() == 'MODULACAO':
            mod = self.tokenizer.next.getstr()
            self.tokenizer.selectNext()
        if self.tokenizer.next.gettokentype() == 'ALTURA':
            nota = self.tokenizer.next.getstr()
        elif self.tokenizer.next.gettokentype() == 'PAUSA':
            nota = self.tokenizer.next.getstr()
        self.tokenizer.selectNext()
        if self.tokenizer.next.gettokentype() == "TO_DUR":
            self.tokenizer.selectNext()
            if self.tokenizer.next.gettokentype() == 'DURACAO':
                dur = self.tokenizer.next.getstr()
                self.tokenizer.selectNext()
                return Nota([nota, mod, dur])


    def parseCompasso(self):
        if self.tokenizer.next.gettokentype() == 'CLAVE':
            self.tokenizer.selectNext()

        lista_compasso = []
        while self.tokenizer.next.gettokentype() != 'FIM_COMPASSO':
            if self.tokenizer.next.gettokentype() == 'FIM_DA_MUSICA':
                break
            nota = self.parseNote()
            lista_compasso.append(nota)
        self.tokenizer.selectNext()
        return Compasso(lista_compasso)

    def parseStatment(self):
        inLoop = False
        if self.tokenizer.next.gettokentype() == "LOOP_START":
            inLoop = True
            self.tokenizer.selectNext()

        p_comp = self.parseCompasso()

        lista_loops = [p_comp]
        while inLoop:
            if self.tokenizer.next.gettokentype() == 'FIM_DE_MUSCIA':
                break
            if self.tokenizer.next.gettokentype() == 'LOOP_END':
                inLoop = False
                self.tokenizer.selectNext()
                return Loop(lista_loops)
            comp = self.parseCompasso()
            lista_loops.append(comp)
        return p_comp


    def parseMusica(self):
        childrenList = []
        if self.tokenizer.next.gettokentype() == "TITULO":
            self.tokenizer.selectNext()
            if self.tokenizer.next.gettokentype() == "ANDAMENTO":
                self.tokenizer.selectNext()
                if self.tokenizer.next.gettokentype() == "COND_ALTURA":
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.gettokentype() == 'CONDITIONAL':
                        self.tokenizer.selectNext()
                        if self.tokenizer.next.gettokentype() == 'DIVISAO_METRICA':
                            self.tokenizer.selectNext()
                            while self.tokenizer.next.gettokentype() != "FIM_DA_MUSICA":
                                childrenList.append(self.parseStatment())
                            return Musica(childrenList)
                        

    def run(self, tokens):
        self.tokenizer = Tokenizer(tokens)
        NodetoReturn = self.parseMusica()

        if self.tokenizer.next.gettokentype() == "FIM_DA_MUSICA":
            return NodetoReturn.Evaluate()

def main():
    text_input = """
    Brilha Brilha Estrelinha;

    tempo = 120;

    C jônio

    4/4

    &G C3:4 C3:4 G3:4 G3:4 ; A3:4 A3:4 G3:4 Z:4 ; F3:4 #E3:4 bF3:4 E3:4 ;
    ||: D3:16 Z:8 C3:16 D3:16 Z:8 E3:16 C3:2 ; :|| Z:1 ||
    """

    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    parser = Parser()
    parser.run(list(tokens))


if __name__ == "__main__":
    main()
