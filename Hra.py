thisdict = {
    "Rychlost": 10,
    "Zdraví": 50,
    "Teplo": 20,
    "Bezpečí": 10,
    "Energie": 10
}
print(thisdict)
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
    thisdict["Zdraví"]= 60
    thisdict["Energie"]= 15
    print(thisdict)
    print("Pořádně ses najedl a napil. +10 zdraví +5 Energie")
    print("Vyber si možnost co uděláš pomocí čísla:")
    print("1 Prohledáváš kryt. Bude tě to stát - 5 energie.")
    print("2 Jdeš se obléknout. Stojí tě to - 3 energie.")
    print("3 Vyrážíš ven.")
    b = input()
    b = int(b)

    # Prohledat kryt.
    if b == 1:
        thisdict["Energie"]= 10
        thisdict["Teplo"]= 30
        print(thisdict)
        print("Našel jsi rukavice a čepici. +10 teplo. Za hledání - 5 energie.")
        print("Co uděláš dále? \n1 Vyrážíš ven \n2 Oblékáš se, stojí tě to - 3 energie \nVyber možnost číslem:")
        c = input()
        c = int(c)

        # Jit ven.
        if c == 1:
            thisdict["Teplo"]= 10
            thisdict["Energie"]= 7
            print(thisdict)
            print("Venku je zima. Teplo -20. Za vynaložené úsilí -3 energie.")

        # Vybirat obleceni.
        elif c == 2:
            thisdict["Energie"]= 7
            print(thisdict)
            print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
            d = input()
            d = int(d)

            # Vzit si triko a kratasy.
            if d == 1:
                thisdict["Teplo"]= 20
                thisdict["Energie"]= 4
                print(thisdict)
                print("Venku mrzne. Triko a kraťasy nebyla nejlepší volba. Teplo -10, energie -3.")

            # Vzit si mikinu a kalhoty.
            elif d == 2:
                thisdict["Teplo"]= 25
                thisdict["Energie"]= 4
                print(thisdict)
                print("Není ti nejlépe. Teplo -5. Energie -3.")

            # Vzit si bundu a zateplene kalhoty.
            elif d == 3:
                thisdict["Teplo"]= 35
                thisdict["Energie"]= 4
                print(thisdict)
                print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")

            # Vzit si kozich.
            elif d == 4:
                thisdict["Teplo"]= 40
                thisdict["Energie"]= 2
                thisdict["Rychlost"]= 8
                print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
            else:
                print("Zvolil jsi špatnou kombinaci")
        else:
            print("Zvolil jsi špatnou kombinaci")

    # Vybrat si obleceni.
    elif b == 2:
        thisdict["Energie"]= 12
        print(thisdict)
        print("Jdeš se obléct. Co si vybereš?")
        print("1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
        c = input()
        c = int(c)

        # Oblect si triko a kratasy.
        if c == 1:
            thisdict["Teplo"]= 12
            print(thisdict)
            print("V triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")

        # Oblect si mikinu a kalhoty.
        elif c == 2:
            thisdict["Teplo"]= 15
            thisdict["Energie"]= 9
            print(thisdict)
            print("Není ti nejlépe. Teplo -5. Není ti nejlépe energie - 3")

        # Oblect si bundu a zateplene kalhoty.
        elif c == 3:
            thisdict["Teplo"]= 25
            thisdict["Energie"]= 12
            print(thisdict)
            print("Ideální možnost do tohoto počasí. Teplo + 5.")

        # Vzit si kozich
        elif c == 4:
            thisdict["Teplo"]= 40
            thisdict["Energie"]= 7
            thisdict["Rychlost"]= 8
            print(thisdict)
            print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
        else:
            print("Zvolil jsi špatnou kombinaci")

    # Jit ven.
    elif b == 3:
        thisdict["Teplo"]= 0
        thisdict["Zdraví"]= 0
        print(thisdict)
        print("Zabouchli se za tebou dveře do krytu. Bez oblečení ses ocitl v mrazivém počasí. Do pár hodin umrzáš.")
        print("Konec hry \nZkus to znovu")
    else:
        print("Zvolil jsi špatnou kombinaci, zkus to znovu:")

# Jdes si vybirat obleceni.
elif a == 2:
    thisdict["Zdraví"]= 40
    print(thisdict)
    print("Oblékáš se a u toho nešíkovně shodíš sklenici s džusem do jídla, proto jsi hladový a žíznivý. -10 zdraví")
    print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
    c = input()
    c = int(c)

    # Oblect si triko a kratasy.
    if c == 1:
        thisdict["Energie"]= 7
        thisdict["Teplo"]= 10
        print(thisdict)
        print("V triku je v mrazivém počasí zima. -10 teplo, energie -3. \nJe ti chladno, co uděláš. \nZvol číslo :")

    # Oblect si mikinu a kalhoty.
    elif c == 2:
        thisdict["Teplo"]= 15
        thisdict["Energie"]= 7
        print(thisdict)
        print("Není ti nejlépe. Teplo -5. Energie -3.")

    # Oblect si bundu a zateplene kalhoty.
    elif c == 3:
        thisdict["Teplo"]= 25
        thisdict["Energie"]= 7
        print(thisdict)
        print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")

    #Oblect si kozich.
    elif c == 4:
        thisdict["Teplo"]= 30
        thisdict["Energie"]= 5
        thisdict["Rychlost"]= 8
        print(thisdict)
        print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")

# Vyrazis ven.
elif a == 3:
    thisdict["Teplo"]= 0
    thisdict["Zdraví"]= 0
    print(thisdict)
    print("Vyrážíš ven hladový a žíznivý. V mrazu nejsi schopný nic udělat. Navíc se za tebou zavřeli dveře do krytu. Umrzl jsi.")
    print("Konec hry \nZkus to znovu")

# Zustavas v krytu.
elif a == 4:
    thisdict["Teplo"]= 30
    thisdict["Zdraví"]= 40
    thisdict["Energie"]= 20
    print(thisdict)
    print("Jdeš opět spát a trávíš čas v krytu. Odpočinul sis. Energie + 10. Objevil jsi i rukavice a čepici. Teplo + 10. Žiješ pokojně dokud nepřijde hlad a žízeň. Zdraví - 10. A ty musíš ven.")
    print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
    b = input()
    b = int(b)

    # Oblekas si triko a kratasy.
    if b == 1:
        thisdict["Energie"]= 17
        thisdict["Teplo"]= 20
        print(thisdict)
        print("V triku je v mrazivém počasí zima. -10 teplo, energie -3\nJe ti chladno, co uděláš. \nZvol číslo :")

    # Oblekas si mikinu a kalhoty.
    elif b == 2:
        thisdict["Teplo"]= 20
        thisdict["Energie"]= 17
        print(thisdict)
        print("Není ti nejlépe. Teplo -5. Energie -3.")

    # Oblekas si bundu a zateplene kalhoty.
    elif b == 3:
        thisdict["Teplo"]= 30
        thisdict["Energie"]= 17
        print(thisdict)
        print("Ideální možnost do tohoto počasí. Teplo + 5. Energie -3.")

    # Oblekas si kozich.
    elif b == 4:
        thisdict["Teplo"]= 35
        thisdict["Energie"]= 17
        thisdict["Rychlost"]= 8
        print(thisdict)
        print("Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
else:
    print("Zvolil jsi špatnou kombinaci, zkus to znovu:")