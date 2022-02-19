# Menü für die Struktogrammaufgaben


## Aufgabe 1 Euro-Kuna umrechner
def aufgabe_1():
    # 1 Euro = 7.4 Kuna
    print()
    print("--- Willkommen zum Euro in Kuna Rechner! ---")
    print("Der Umrechnungskurs beträgt 1 Euro = 7.4 Kuna.")
    print()
    eurobetrag=float(input("Bitte geben sie den Betrag in Euro ein: "))
    #Berechnung Kuna
    kuna=eurobetrag*7.4
    print()
    print("Ihr Eurobetrag wären nach dem Umtausch " + str(kuna) + " Kuna")
    print()
    print("Vielen Dank für die Nutzung des Umrechners")
    print()


## Aufgabe 2 Führerscheintest
def aufgabe_2():
    print()
    print("--- Wilkommen zum Führerscheintest. ---")
    print("Lass uns zuerst dein Alter überprüfen")
    print()
    age=int(input("Bitte gib zur Kontrolle dein Alter hier ein: "))

    if age >= 18:
        print()
        print("Herzlichen Glückwunsch! Du darfst den Führerschein machen!")
    else:
        print()
        print("Sorry, du musst noch warten.")
    print()


## Aufgabe 3 Das Zinsproblem
def aufgabe_3():
    print()
    print("---- Willkommen zum Zinsrechner. ----")
    print()
    print("Wie lange brauchen ??? Euro bei 4.5% Zins bis sich das Geld verdreifacht hat?")
    print()

    e=float(input("Bitte den Betrag in Euro eingeben: "))
    #e=float(380)
    s=e
    j=int(0)
    z=0
    print()
    while s < (e*3):
        z=float((s*0.045))
        s=(s+z)
        j=j+1
        print("Nach dem " + str(j) + ". Jahr: " + str(s) + " Euro   (Zins: " + str(z) + " Euro)")
    print()    

    print("Der Geldbetrag hat sich nach " + str(j) + " Jahren verdreifacht.")
    print()
    
    
## Aufgabe 4 Kindergeld
def aufgabe_4():
    print()
    print("--- Wilkommen zum Kindergeld Rechner! ---")
    print()
    print("Kindergeld wird nur gezahlt, wenn die Familie genau 2 Kinder hat.")
    print("Ebenso darf das Alter eines Kindes 18 Jahre nicht überschreiten.")
    print("Wenn zum Beispiel eine Familie 2 Kinder hat und eines 18 Jahre alt ist,")
    print("wird nur für 1 Kind Kindergeld bezahlt. Kindergeld beträgt pro Kind 100 Euro.")
    print()
    anzahl_kinder=int(input("Bitte geben sie die Anzahl Ihrer Kinder ein: "))
    print()

    if anzahl_kinder == 2:
        age_kind1=int(input("Bitte geben sie das Alter Ihres ersten Kindes ein: "))
        age_kind2=int(input("Bitte geben sie das Alter Ihres zweiten Kindes ein: "))
        if age_kind1<18:
            if age_kind2<18:
                print()
                print("Sie bekommen 200€ Kindergeld!")
            else:
                print()
                print("Sie bekommen 100€ Kindergeld!")
        else:
            if age_kind2<18:
                print()
                print("Sie bekommen 100€ Kindergeld!")
            else:
                print()
                print("Sie bekommen leider kein Kindergeld.")
    else:
        print()
        print("Sie bekommen leider kein Kindergeld.")
    print()
    
    
## Aufgabe 5.1 Die Strafarbeit
def aufgabe_5():
    countdown=int(50)
    countdown_old=countdown
    text=("0")
    value=("Ich muss immer meine Hausaufgaben machen.")
    cheat_value=("Hallo Welt!")
    wrong=int(0)

    print()
    print("Du Musst eine Strafarbeit machen!!!!!")
    print("Es wird von dir verlangt folgenden Satz 50 mal genau(!) einzugeben:")
    print()
    print(value)
    print()
    
    print("Los geht's...")
    print('Versuche es doch mal mit "Hallo Welt!" ;)')
    while countdown != 0:
        pain_value=str(input("Hier eingeben: "))
        if pain_value==value:
            countdown=countdown-1
            print("Super du musst nur noch " + str(countdown) + " mal schreiben!")
            print()
        elif pain_value==cheat_value:
            countdown=0
            print("Cheat accepted!")
            print()
        else:
            print("Du hattest einen Fehler, bitte versuche es noch einmal")
            wrong=wrong+1
            print()
            
    print("Toll! Du hast es geschafft!")
    print()
    print("Du hast den satz: " + value)
    print("erfolgreich " + str(countdown_old) + " mal fehlerfrei geschrieben.")
    print(str(wrong) + (" mal hattest du Fehler"))
    print()


## Start des Programmms

print()
print(" █████ ███████████            █████ █████  ████      ")
print(" ░███ ░█░░░███░░░█           ░░███ ░░███  ░░███      ")
print(" ░███ ░   ░███  ░             ░███  ░███ █ ░███      ")
print(" ░███     ░███     ██████████ ░███████████ ░███      ")
print(" ░███     ░███    ░░░░░░░░░░  ░░░░░░░███░█ ░███      ")
print(" ░███     ░███                      ░███░  ░███      ")
print(" █████    █████                     █████  █████     ")
print("░░░░    ░░░░░                     ░░░░░  ░░░░░       ")
                                                
print()
print("Bitte das gewünschte Programm auswählen:")
print("1 ~  Euro - Kuna Umrechner")
print("2 ~  Führerscheintest")
print("3 ~  Zinsproblem")
print("4 ~  Kindergeld")
print("5 ~  Die Strafarbeit")
print("0 ~  Beenden")
print()

x=int(input("Bitte Auswahl hier eingeben: "))

while x>5:
    print()
    print()
    print("FEHLER! Erneut versuchen!")
    print()
    print("Bitte das gewünschte Programm auswählen:")
    print("1 ~  Euro - Kuna Umrechner")
    print("2 ~  Führerscheintest")
    print("3 ~  Zinsproblem")
    print("4 ~  Kindergeld")
    print("5 ~  Die Strafarbeit")
    print("0 ~  Beenden")
    print()
    x=int(input("Bitte Auswahl hier eingeben: "))


if x==1:
    print("Starte Programm " + str(x) + "...")
    print("------------------------------------------------------------------")
    aufgabe_1()
elif x==2:
    print("Starte Programm " + str(x) + "...")
    print("------------------------------------------------------------------")
    aufgabe_2()
elif x==3:
    print("Starte Programm " + str(x) + "...")
    print("------------------------------------------------------------------")
    aufgabe_3()
elif x==4:
    print("Starte Programm " + str(x) + "...")
    print("------------------------------------------------------------------")
    aufgabe_4()
elif x==5:
    print("Starte Programm " + str(x) + "...")
    print("------------------------------------------------------------------")
    aufgabe_5()
elif x==0:
        print("Beenden")
        print()
        
##Programmende
