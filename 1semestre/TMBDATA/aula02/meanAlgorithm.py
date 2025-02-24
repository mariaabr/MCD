# algoritmo para a media em streaming >> sem memoria

stream = [1.5, 2, 25, 4, 7.5, 3, 9, 4.5] # initialize stream list

class BaseAlg: # algorithm class
    stream = []
    results = {}
    x = 0 # each x is an element of the stream list

    # other variables
    A = 0
    n = 0

    def alg(self):
        A = A + x
        n += 1

        S = A/n

    def verify(self):
        ...
    
class StreamAlg(BaseAlg): # another class
    def _init_(self, stream):
        self.stream = stream
        self.exec()
        self.verify()

    def exec(self):
        for v in self.stream:
            self.x = v
            self.alg()
        print(self.results)

# SA = StreamAlg(BaseAlg) # nao passei direito

# nao funciona porque a media final so se tem no fim, ao longo do argoritmo existem varias media e o "u" so vai chegar no fim