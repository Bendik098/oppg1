import random


print("kan du gjette hvilke tall jeg tenker på?")


korrekt_svar = random.randint(1,10)



while True:

    try:


        bruker_svar = int(input("Skriv inn tallet du tror jeg tenker på!"))


        if korrekt_svar == bruker_svar:
            print ("Bra! Du klarte det!")
            break
        elif korrekt_svar == bruker_svar + 1 or korrekt_svar == bruker_svar - 1:
            print("desverre du bommet med 1")
        elif bruker_svar == 0:
            print("akk for at du spilte")
            break

        else:
            print("Feil prøv på nytt")       

    except ValueError:
        print("Du må skrive ett tall uten desimaler! ")
