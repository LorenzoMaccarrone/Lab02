import dictionary
d=dictionary.Dictionary()
class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print(f" # 1. Aggiungi nuova parola \n "
              f"# 2. Cerca una traduzione \n"
              f" # 3. Cerca con wildcard\n"
              f" # 4. Exit\n"
              f" # 5 stampa dizionario corrrente\n")
        pass

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        f= open(dict,"r")
        righe=f.readlines()
        for r in righe:
            riga=r.split()
            d.addWord(riga[0], riga[1])

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...> NO?
        #in ingresso ho una stringa che mi viene passata dall'utente
        #perchè dovrei volerla trattare come una tupla???
        parole=entry.split()
        d.addWord(parole[0], parole[1])


    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        traduzione=d.translate(query)
        if traduzione is not(None):
            print(traduzione)
        else:
            print("Mi dispiace ma la parola cerata non esiste")



    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass
    def stampaDizionario(self):
        dizionario=d.ottieniDzionario()
        for p in dizionario:
            print(p)