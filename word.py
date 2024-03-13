class Word:
    def __init__(self, parola_aliena, parola_italiana):
        self._parola_aliena=parola_aliena
        self._parola_italiana=parola_italiana
    def __str__(self):
        return f"{self._parola_aliena} {self._parola_italiana}"




