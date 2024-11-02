Rychlost = 10
Zdraví = 50
Teplo = 20
Bezpečí = 10
Energie = 10
print(f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {Teplo} \nBezpečí : {Bezpečí} \nEnergie: {Energie}\n")
print("Probudil jsi se ve spodním prádle a u postele leží boty, které si obouváš.")
print("Vyber si možnost co uděláš pomocí čísla:")
print("1 Jdeš se najíst a napít džusu.")
print("2 Jdeš se obléct.")
print("3 Vyrazíš ven.")
print("4 Jdeš opět spát a trávíš čas v krytu.")
print("Vlož číslo:")
a = input()
a = int(a)

if a == 1:
    Z = Zdraví + 10
    E = Energie + 5
    print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {Teplo} \nBezpečí : {Bezpečí} \nEnergie : {E}")
    print("Pořádně ses najedl a napil. +10 zdraví +5 Energie")
    print("Vyber si možnost co uděláš pomocí čísla:")
    print("1 Prohledáváš kryt. Bude tě to stát - 5 energie.")
    print("2 Jdeš se obléknout. Stojí tě to - 3 energie.")
    print("3 Vyrážíš ven.")
    b = input()
    b = int(b)

    if b == 1:
        E1 = E - 5
        T1 = Teplo + 10
        print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T1} \nBezpečí : {Bezpečí} \nEnergie : {E1}")
        print("Našel jsi rukavice a čepici. +10 teplo. Za hledání - 5 energie.")
        print("Co uděláš dále? \n1 Vyrážíš ven \n2 Oblékáš se, stojí tě to - 3 energie \nVyber možnost číslem:")
        c = input()
        c = int(c)

        if c == 1:
            T2 = T1 - 20
            E2 = E1 - 3
            MoznostA = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T2} \nBezpečí {Bezpečí} \nEnergie : {E2}")
            print(MoznostA)
            print("Venku je zima. Teplo -20. Za vynaložené úsilí -3 energie.")
            if T2 <= 0:
                print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T2} \nBezpečí : {Bezpečí} \nEnergie : {E2}")
                print("Zabouchli se za tebou dveře do krytu. Bez oblečení ses ocitl v mrazivém počasí. Do pár hodin umrzáš.")
            elif T2 > 0:
                print("Jsi venku.")
        elif c == 2:
            E3 = E1 - 3
            print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T1} \nBezpečí : {Bezpečí} \nEnergie : {E3}")
            print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
            d = input()
            d = int(d)
            if d == 1:
                T2 = T1 - 10
                E4 = E3 - 3
                MoznostB = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T2} \nBezpečí : {Bezpečí} \nEnergie : {E4}")
                print(MoznostB)
                print("Venku mrzne. Triko a kraťasy nebyla nejlepší volba. Teplo -10, energie -3.")
            elif d == 2:
                T2 = T1 - 5
                E4 = E3 - 3
                MoznostC = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T2} \nBezpečí : {Bezpečí} \nEnergie : {E4}")
                print(MoznostC)
                print("Není ti nejlépe. Teplo -5. Energie -3.")
            elif d == 3:
                T2 = T1 + 5
                E4 = E3 - 3
                MoznostD = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T2} \nBezpečí : {Bezpečí} \nEnergie : {E4}")
                print(MoznostD)
                print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")
            elif d == 4:
                T2 = T1 + 10
                R = Rychlost - 2
                E4 = E3 - 5
                MoznostE = (f"Rychlost : {R} \nZdraví : {Z} \nTeplo : {T2} \nBezpečí : {Bezpečí} \nEnergie : {E4}")
                print(MoznostE)
                print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
            else:
                print("Zvolil jsi špatnou kombinaci")
        else:
            print("Zvolil jsi špatnou kombinaci")

    elif b == 2:
        E = Energie - 3
        Moznost1A = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {Teplo} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print("Jdeš se obléct. Co si vybereš?")
        print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
        c = input()
        c = int(c)
        if c == 1:
            T1 = Teplo - 10
            Moznost1A = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T1} \nBezpečí : {Bezpečí} \nEnergie : {E}")
            print(Moznost1A)
            print("V triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")
        elif c == 2:
            T2 = Teplo - 5
            Moznost1B = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T2} \nBezpečí : {Bezpečí} \nEnergie : {E}")
            print(Moznost1B)
            print("Není ti nejlépe. Teplo -5. Energie -3.")
        elif c == 3:
            T3 = Teplo + 5
            E1 = E - 3
            Moznost1C = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T3} \nBezpečí : {Bezpečí} \nEnergie : {E1}")
            print(Moznost1C)
            print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")
        elif c == 4:
            T4 = Teplo + 10
            R = Rychlost - 2
            E2 = E - 5
            Moznost1D = (f"Rychlost : {R} \nZdraví : {Z} \nTeplo : {T4} \nBezpečí : {Bezpečí} \nEnergie : {E2}")
            print(Moznost1D)
            print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
        else:
            print("Zvolil jsi špatnou kombinaci")

    elif b == 3:
        T = Teplo - 20
        print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print("Zabouchli se za tebou dveře do krytu. Bez oblečení ses ocitl v mrazivém počasí. Do pár hodin umrzáš.")
        print("Konec hry \nZkus to znovu")
    else:
        print("Zvolil jsi špatnou kombinaci, zkus to znovu:")

elif a == 2:
    Z = Zdraví - 10
    print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {Teplo} \nBezpečí : {Bezpečí} \nEnergie : {Energie}")
    print("Oblékáš se a u toho nešíkovně shodíš sklenici s džusem do jídla, proto jsi hladový a žíznivý. -10 zdraví")
    print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
    c = input()
    c = int(c)
    if c == 1:
        E = Energie - 3
        T = Teplo - 10
        Moznost2A = (f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print(Moznost2A)
        print("V triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")
    elif c == 2:
        E = Energie - 3
        T1 = Teplo - 5
        Moznost2B = (f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {T1} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print(Moznost2B)
        print("Není ti nejlépe. Teplo -5. Energie -3.")
    elif c == 3:
        T2 = Teplo + 5
        E1 = Energie - 3
        Moznost2C = (f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {T2} \nBezpečí : {Bezpečí} \nEnergie : {E1}")
        print(Moznost2C)
        print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")
    elif c == 4:
        T3 = Teplo
        R = Rychlost - 2
        E2 = Energie - 3
        Moznost1D = (f"Rychlost : {R} \nZdraví : {Zdraví} \nTeplo : {T3} \nBezpečí : {Bezpečí} \nEnergie : {E2}")
        print(Moznost1D)
        print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")


elif a == 3:
    T = Teplo - 20
    Z = Zdraví - 10
    print(f"Rychost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {Energie}")
    print("Vyrážíš ven hladový a žíznivý. V mrazu nejsi schopný nic udělat. Navíc se za tebou zavřeli dveře do krytu. Umrzl jsi.")
    print("Konec hry \nZkus to znovu")

elif a == 4:
    T = Teplo + 10
    Z = Zdraví - 10
    E = Energie + 10
    print(f"Rychost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
    print("Jdeš opět spát a trávíš čas v krytu. Odpočinul sis. Energie + 10. Objevil jsi i rukavice a čepici. Teplo + 10. Žiješ pokojně dokud nepřijde hlad a žízeň. Zdraví - 10. A ty musíš ven.")
    print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
    d = input()
    d = int(d)
    if d == 1:
        T1 = Teplo - 10
        E = Energie - 3
        Moznost1D = (f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {T1} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print(Moznost1D)
        print("V triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")
    elif d == 2:
        E = Energie - 3
        T2 = Teplo - 5
        Moznost2D = (f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {T2} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print(Moznost2D)
        print("Není ti nejlépe. Teplo -5. Energie -3.")
    elif d == 3:
        T3 = Teplo + 5
        E = Energie - 3
        Moznost3D = (f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {T3} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print(Moznost3D)
        print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")
    elif d == 4:
        T4 = Teplo + 10
        R = Rychlost - 2
        E = Energie - 3
        Moznost4D = (f"Rychlost : {R} \nZdraví : {Zdraví} \nTeplo : {T4} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print(Moznost4D)
        print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
else:
    print("Zvolil jsi špatnou kombinaci, zkus to znovu:")

Rychlost = 10
Rychlost1 = 8
Zdraví = 60
Zdraví1 = 50
Teplo = 10
Teplo1 = 25
Teplo2 = 15
Bezpečí = 10
Energie = 7
Energie1 = 4
Zacatek = MoznostA = Moznost1A = print(f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {Teplo} \nBezpečí : {Bezpečí} \nEnergie: {Energie}")
Zacatek1 = MoznostC = Moznost1B = print(f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {Teplo1} \nBezpečí : {Bezpečí} \nEnergie: {Energie1}")
Zacatek2 = Moznost2A = Moznost1D = print(f"Rychlost : {Rychlost} \nZdraví : {Zdraví1} \nTeplo : {Teplo} \nBezpečí : {Bezpečí} \nEnergie: {Energie}")
Zacatek3 = Moznost3B = Moznost2D = print(f"Rychlost : {Rychlost} \nZdraví : {Zdraví1} \nTeplo : {Teplo2} \nBezpečí : {Bezpečí} \nEnergie: {Energie}")




