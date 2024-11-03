Atribut = {
    "Rychlost": 10,
    "Zdraví": 50,
    "Teplo": 20,
    "Bezpečí": 10,
    "Energie": 10
}
print(Atribut)
print("Probudil jsi se ve spodním prádle a u postele leží boty, které si obouváš.")
print("Vyber si možnost co uděláš pomocí čísla:")
print("1 Jdeš se najíst a napít džusu.")
print("2 Jdeš se obléct.")
print("3 Vyrazíš ven.")
print("4 Jdeš opět spát a trávíš čas v krytu.")
print("Vlož číslo:")
a = input()
a = int(a)

# Najist se a napit.
if a == 1:
    Atribut["Zdraví"]= 60
    Atribut["Energie"]= 15
    print(Atribut)
    print("Pořádně ses najedl a napil. +10 zdraví +5 Energie")
    print("Vyber si možnost co uděláš pomocí čísla:")
    print("1 Prohledáváš kryt. Bude tě to stát - 5 energie.")
    print("2 Jdeš se obléknout. Stojí tě to - 3 energie.")
    print("3 Vyrážíš ven.")
    b = input()
    b = int(b)

    # Prohledat kryt.
    if b == 1:
        Atribut["Energie"]= 10
        Atribut["Teplo"]= 30
        print(Atribut)
        print("Našel jsi rukavice a čepici. +10 teplo. Za hledání - 5 energie.")
        print("Co uděláš dále? \n1 Vyrážíš ven \n2 Oblékáš se, stojí tě to - 3 energie \nVyber možnost číslem:")
        c = input()
        c = int(c)

        # Jit ven.
        if c == 1:
            Atribut["Teplo"]= 10
            Atribut["Energie"]= 7
            print(Atribut)
            print("Venku je zima. Teplo -20. Za vynaložené úsilí -3 energie.")
            print("Jsi venku, kde sněží. Přemýšlíš co uděláš.")
            print("1 Najdeš vodu. -2 energie \n2 Vytvoříš pasti. \n3 Hledáš skrýš a vztváříš oheň. \nZvol číslo:")
            d = input()
            d = int(d)

            #Hledáš vodu.
            if d == 1:
                Atribut["Energie"]= 2
                print(Atribut)
                print("Našel jsi průzračné jezero plné ryb. Napadlo tě nějakou si ulovit. \nVytváříš si z klacku a ostrého kamene harpunu. -5 energie")
                print("1 Sníš syrovou rybu. \n2 Rozděláš oheň. - 3 energie \n3 Hledáš úkryt, kde rozděláš oheň - 6 energie\nVyber číslo:")
                e = input()
                e = int(e)

                #Syrová ryba
                if e == 1:
                    Atribut["Zdraví"]=65
                    Atribut["Teplo"]=5
                    print(Atribut)
                    print("Snědl jsi syrovou rybu. + 5 zdraví - 5 teplo")

                #Rozděláš oheň
                if e == 2:
                    Atribut["Energie"]= 0
                    Atribut["Bezpečí"]= 0
                    Atribut["Zdraví"]= 30
                    print(Atribut)
                    print("U rozdělávání ohně usneš. Energie -2 Bezpečí - 10. Napadl tě medvěd. Zabil jsi jej harpunou. Zdraví -30")
                    Atribut["Energie"]= 15
                    Atribut["Zdraví"]= 35
                    Atribut["Bezpečí"]= 5
                    Atribut["Teplo"]= 20
                    print(Atribut)
                    print("Po vyhraném boji dospáváš. + 10 energie \nRozděláš oheň a opečeš rybu. + 5 zdraví + 5 energie + 5 bezpečí")

                #Hledáš skrýš a rozděláš oheň.
                if e == 3:
                    Atribut["Energie"]= 0
                    Atribut["Bezpečí"]= 0
                    Atribut["Teplo"]= 0
                    Atribut["Zdraví"]= 0
                    print(Atribut)
                    print("Nemáš dostatek energie. Usínáš pomalu umrzáš. Navíc tě napadá medvěd. Nemáš se jak bránit. Umíráš.")
                    print("Konec hry")

        # Vybirat obleceni.
        elif c == 2:
            Atribut["Energie"]= 7
            print(Atribut)
            print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
            d = input()
            d = int(d)

            # Vzit si triko a kratasy.
            if d == 1:
                Atribut["Teplo"]= 20
                Atribut["Energie"]= 4
                print(Atribut)
                print("Venku mrzne. Triko a kraťasy nebyla nejlepší volba. Teplo -10, energie -3.")

            # Vzit si mikinu a kalhoty.
            elif d == 2:
                Atribut["Teplo"]= 25
                Atribut["Energie"]= 4
                print(Atribut)
                print("Není ti nejlépe. Teplo -5. Energie -3.")

            # Vzit si bundu a zateplene kalhoty.
            elif d == 3:
                Atribut["Teplo"]= 35
                Atribut["Energie"]= 4
                print(Atribut)
                print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")

            # Vzit si kozich.
            elif d == 4:
                Atribut["Teplo"]= 40
                Atribut["Energie"]= 2
                Atribut["Rychlost"]= 8
                print(Atribut)
                print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
            else:
                print("Zvolil jsi špatnou kombinaci")
        else:
            print("Zvolil jsi špatnou kombinaci")

    # Vybrat si obleceni.
    elif b == 2:
        Atribut["Energie"]= 12
        print(Atribut)
        print("Jdeš se obléct. Co si vybereš?")
        print("1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
        c = input()
        c = int(c)

        # Oblect si triko a kratasy.
        if c == 1:
            Atribut["Teplo"]= 12
            print(Atribut)
            print("V triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")

        # Oblect si mikinu a kalhoty.
        elif c == 2:
            Atribut["Teplo"]= 15
            Atribut["Energie"]= 9
            print(Atribut)
            print("Není ti nejlépe. Teplo -5. Není ti nejlépe energie - 3")

        # Oblect si bundu a zateplene kalhoty.
        elif c == 3:
            Atribut["Teplo"]= 25
            Atribut["Energie"]= 12
            print(Atribut)
            print("Ideální možnost do tohoto počasí. Teplo + 5.")

        # Vzit si kozich
        elif c == 4:
            Atribut["Teplo"]= 40
            Atribut["Energie"]= 7
            Atribut["Rychlost"]= 8
            print(Atribut)
            print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
        else:
            print("Zvolil jsi špatnou kombinaci")

    # Jit ven.
    elif b == 3:
        Atribut["Teplo"]= 0
        Atribut["Zdraví"]= 0
        print(Atribut)
        print("Zabouchli se za tebou dveře do krytu. Bez oblečení ses ocitl v mrazivém počasí. Do pár hodin umrzáš.")
        print("Konec hry \nZkus to znovu")
    else:
        print("Zvolil jsi špatnou kombinaci, zkus to znovu:")

    # Jdes si vybirat obleceni.
elif a == 2:
    Atribut["Zdraví"]= 40
    print(Atribut)
    print("Oblékáš se a u toho nešíkovně shodíš sklenici s džusem do jídla, proto jsi hladový a žíznivý. -10 zdraví")
    print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
    c = input()
    c = int(c)

    # Oblect si triko a kratasy.
    if c == 1:
        Atribut["Teplo"] = 10
        print(Atribut)
        print("V triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")

    # Oblect si mikinu a kalhoty.
    elif c == 2:
        Atribut["Teplo"] = 15
        Atribut["Energie"] = 7
        print(Atribut)
        print("Není ti nejlépe. Teplo -5. Není ti nejlépe energie - 3")

    # Oblect si bundu a zateplene kalhoty.
    elif c == 3:
        Atribut["Teplo"] = 15
        Atribut["Energie"] = 7
        print(Atribut)
        print("Není ti nejlépe. Teplo -5. Energie -3.")

    # Vzit si kozich
    elif c == 4:
        Atribut["Teplo"] = 30
        Atribut["Energie"] = 5
        Atribut["Rychlost"] = 8
        print(Atribut)
        print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
    else:
        print("Zvolil jsi špatnou kombinaci.")

# Vyrazis ven.
elif a == 3:
    Atribut["Teplo"]= 0
    Atribut["Zdraví"]= 0
    print(Atribut)
    print("Vyrážíš ven hladový a žíznivý. V mrazu nejsi schopný nic udělat. Navíc se za tebou zavřeli dveře do krytu. Umrzl jsi.")
    print("Konec hry \nZkus to znovu")

# Zustavas v krytu.
elif a == 4:
    Atribut["Teplo"]= 30
    Atribut["Zdraví"]= 40
    Atribut["Energie"]= 20
    print(Atribut)
    print("Jdeš opět spát a trávíš čas v krytu. Odpočinul sis. Energie + 10. Objevil jsi i rukavice a čepici. Teplo + 10. Žiješ pokojně dokud nepřijde hlad a žízeň. Zdraví - 10. A ty musíš ven.")
    print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
    b = input()
    b = int(b)

    # Oblekas si triko a kratasy.
    if b == 1:
        Atribut["Energie"]= 17
        Atribut["Teplo"]= 20
        print(Atribut)
        print("V triku je v mrazivém počasí zima. -10 teplo, energie -3\nJe ti chladno, co uděláš. \nZvol číslo :")

    # Oblekas si mikinu a kalhoty.
    elif b == 2:
        Atribut["Teplo"]= 20
        Atribut["Energie"]= 17
        print(Atribut)
        print("Není ti nejlépe. Teplo -5. Energie -3.")

    # Oblekas si bundu a zateplene kalhoty.
    elif b == 3:
        Atribut["Teplo"]= 30
        Atribut["Energie"]= 17
        print(Atribut)
        print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")

    # Oblekas si kozich.
    elif b == 4:
        Atribut["Teplo"]= 35
        Atribut["Energie"]= 17
        Atribut["Rychlost"]= 8
        print(Atribut)
        print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
    else:
        print("Zvolil jsi špatnou kombinaci, zkus to znovu:")