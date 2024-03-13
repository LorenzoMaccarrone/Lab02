import translator as tr #con questo importiamo il modulo translator nel main

'''
con questo ci evitiamo di chiaamre ogni volta tr.Translator().quello_che_mi_serve
ma sscrivere semplicemente t.quello_che_mi_serve
'''
t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")


    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        input1 = input(print("Dimmi la nuova parola da AGGIUNGERE"))
        #controlla che vengano inserite solo parole con a-z o A-Z
        input2=input1.split()
        if input2[0].isalpha() and input2[1].isalpha():
            input1=input1.lower()
            t.handleAdd(input1)
            print("Parola aggiunta!")
        else:
            print("Parola non valida!")
        pass

    if int(txtIn) == 2:
        input1 = input(print("Dimmi la nuova parola da CERCARE"))
        input2=input1.lower()
        t.handleTranslate(input2)
        pass

    if int(txtIn) == 3:
        print("In fase di sviluppo...")
        pass

    if int(txtIn) == 4:
        break
    if int(txtIn) == 5:
        t.stampaDizionario()
        pass
