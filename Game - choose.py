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
        E = E - 5
        T = Teplo + 10
        print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print("Našel jsi rukavice a čepici. +10 teplo. Za hledání - 5 energie.")
        print("Co uděláš dále? \n1 Vyrážíš ven \n2 Oblékáš se, stojí tě to - 3 energie \nVyber možnost číslem:")
        c = input()
        c = int(c)

        if c == 1:
            T = T - 20
            E = E - 3
            MoznostA = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí {Bezpečí} \nEnergie : {E}")
            print(MoznostA)
            print("Venku je zima. Teplo -20. Za vynaložené úsilí -3 energie.")
            if T <= 0:
                print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
                print("Zabouchli se za tebou dveře do krytu. Bez oblečení ses ocitl v mrazivém počasí. Do pár hodin umrzáš.")
            elif T > 0:
                print("Jsi venku.")
        elif c == 2:
            E = E - 3
            print(f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
            print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
            d = input()
            d = int(d)
            if d == 1:
                T = T - 10
                E = E - 3
                MoznostB = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
                print(MoznostB)
                print("Venku mrzne. Triko a kraťasy nebyla nejlepší volba. Teplo -10, energie -3.")
            elif d == 2:
                T = T - 5
                E = E - 3
                MoznostC = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
                print(MoznostC)
                print("Není ti nejlépe. Teplo -5. Energie -3.")
            elif d == 3:
                T = T + 5
                E = E - 3
                MoznostD = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
                print(MoznostD)
                print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")
            elif d == 4:
                T = T + 10
                R = Rychlost - 2
                E = E - 5
                MoznostE = (f"Rychlost : {R} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
                print(MoznostE)
                print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
            else:
                print("Zvolil jsi špatnou kombinaci")
        else:
            print("Zvolil jsi špatnou kombinaci")

    elif b == 2:
        E = Energie - 3
        print("Jdeš se obléct. Co si vybereš?")
        print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
        c = input()
        c = int(c)
        if c == 1:
            E = E - 3
            T = Teplo - 10
            Moznost1A = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
            print(Moznost1A)
            print("V triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")
        elif c == 2:
            E = E - 3
            T = Teplo - 5
            Moznost1B = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
            print(Moznost1B)
            print("Není ti nejlépe. Teplo -5. Energie -3.")
        elif c == 3:
            T = Teplo + 5
            E = E - 3
            Moznost1C = (f"Rychlost : {Rychlost} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
            print(Moznost1C)
            print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")
        elif c == 4:
            T = Teplo + 10
            R = Rychlost - 2
            E = E - 5
            Moznost1D = (f"Rychlost : {R} \nZdraví : {Z} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
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
    Z2 = Zdraví - 10
    print(f"Rychlost : {Rychlost} \nZdraví : {Z2} \nTeplo : {Teplo} \nBezpečí : {Bezpečí} \nEnergie : {Energie}")
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
        T = Teplo - 5
        Moznost2B = (f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print(Moznost2B)
        print("Není ti nejlépe. Teplo -5. Energie -3.")
    elif c == 3:
        T = Teplo + 5
        E = Energie - 3
        Moznost2C = (f"Rychlost : {Rychlost} \nZdraví : {Zdraví} \nTeplo : {T} \nBezpečí : {Bezpečí} \nEnergie : {E}")
        print(Moznost2C)
        print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")


elif a == 3:
    T3 = Teplo - 20
    Z3 = Zdraví - 10
    print(f"Rychost : {Rychlost} \nZdraví : {Z3} \nTeplo : {T3} \nBezpečí : {Bezpečí} \nEnergie : {Energie}")
    print("Vyrážíš ven hladový a žíznivý. V mrazu nejsi schopný nic udělat. Navíc se za tebou zavřeli dveře do krytu. Umrzl jsi.")
    print("Konec hry \nZkus to znovu")

elif a == 4:
    T4 = Teplo + 10
    Z4 = Zdraví - 10
    E4 = Energie + 10
    print(f"Rychost : {Rychlost} \nZdraví : {Z4} \nTeplo : {T4} \nBezpečí : {Bezpečí} \nEnergie : {E4}")
    print("Jdeš opět spát a trávíš čas v krytu. Odpočinul sis. Energie + 10. Objevil jsi i rukavice a čepici. Teplo + 10. Žiješ pokojně dokud nepřijde hlad a žízeň. Zdraví - 10. A ty musíš ven.")
else:
    print("Zvolil jsi špatnou kombinaci, zkus to znovu:")








