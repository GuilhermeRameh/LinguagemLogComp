class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Musica():
    def __init__(self, tempo, andamento, compassos):
        self.tempo=tempo
        self.andamento=andamento
        self.compassos=compassos

    def eval(self):
        DoSomthing(self.tempo, self.andamento, self.compassos)


class Compasso():
    def __init__(self, compasso, compassos):
        self.compasso = compasso
        self.compassos = compassos

    # Nao sei se ta certo
    def eval(self):
        return [self.compasso, self.compassos.eval()]

def DoSomthing():
    pass