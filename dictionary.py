import word

class Dictionary:

    def __init__(self):
        self.dizionario=[] #dizionario è una lista di word
    def addWord(self, parola_aliena, parola_italiana):
            self.dizionario.append(word.Word(parola_aliena, parola_italiana))

    def translate(self,parola_aliena):
        for p in self.dizionario:
            if p._parola_aliena==parola_aliena:
                return p
    def translateWordWildCard(self):
        pass
    def ottieniDzionario(self):
        return self.dizionario
