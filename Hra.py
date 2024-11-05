from My_project.Hello_world import Zdraví

Atribut = {
    "Rychlost": 10,
    "Zdraví": 50,
    "Teplo": 20,
    "Bezpečí": 10,
    "Energie": 10
}
print(Atribut)
print("\nProbudil jsi se ve spodním prádle a u postele leží boty, které si obouváš.")
print("\nVyber si možnost co uděláš pomocí čísla:")
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
    print("\nPořádně ses najedl a napil. +10 zdraví +5 Energie")
    print("\nVyber si možnost co uděláš pomocí čísla:")
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
        print("\nNašel jsi rukavice a čepici. +10 teplo. Za hledání - 5 energie.")
        print("\nCo uděláš dále? \n1 Vyrážíš ven \n2 Oblékáš se, stojí tě to - 3 energie \nVyber možnost číslem:")
        c = input()
        c = int(c)

        # Jit ven.
        if c == 1:
            Atribut["Teplo"]= 10
            Atribut["Energie"]= 7
            print(Atribut)
            print("\nVenku je zima. Teplo -20. Za vynaložené úsilí -3 energie.")
            print("\nJsi venku, kde sněží. Přemýšlíš co uděláš.")
            print("1 Najdeš vodu. -4 energie \n2 Vytvoříš pasti. \n3 Hledáš skrýš a vytváříš oheň. \nZvol číslo:")
            d = input()
            d = int(d)

            #Hledáš vodu.
            if d == 1:
                Atribut["Energie"]= 3
                Atribut["Zdraví"]= 65
                print(Atribut)
                print("\nNašel jsi průzračné jezero plné ryb. + 5 zdraví Vysekáváš díru do ledu. Napadlo tě nějakou rybu si ulovit. \nVytváříš si z klacku a ostrého kamene harpunu. -5 energie")
                print("1 Sníš syrovou rybu. \n2 Rozděláš oheň. - 3 energie \n3 Hledáš úkryt, kde rozděláš oheň - 6 energie\nVyber číslo:")
                e = input()
                e = int(e)

                # Syrová ryba.
                if e == 1:
                    Atribut["Zdraví"] = 65
                    Atribut["Teplo"] = 5
                    print(Atribut)
                    print("\nSnědl jsi syrovou rybu. + 5 zdraví - 5 teplo")

                    # Rozděláváš oheň.
                    Atribut["Energie"]= 0
                    Atribut["Bezpečí"] = 5
                    Atribut["Zdraví"] = 30
                    Atribut["Teplo"] = 15
                    print(Atribut)
                    print("\nRozděláváš oheň ze zbytku sil. - 3 energie - 5 bezpečí +10 teplo. Ve spánku tě apadá tě vlk. Nemáš čím se bránit, proto se snažíš utéct. Zdraví - 35")
                    Atribut["Energie"] = 10
                    print(Atribut)
                    print("\nJdeš spát z vyčerpání.")
                    print('Před sebou vidíš hrad, stara chatka, jeskyne \nKam se vydáš, napiš možnost, jak je v zadání:')
                    f = input()

                    #Hrad
                    if f == "hrad":
                        Atribut["Bezpečí"] = -5
                        Atribut["Zdraví"] = 0
                        print(Atribut)
                        print("\nBlížíš se k hradu a všichni se na tebe zvláštně koukají. Po příchodu ke vchodu se tě ptá stráž na povolení,")
                        print("které nemáš a tak tě zničeho nic napadnou. Bezpečí - 10, Zdraví - 30.")
                        print("Bohužel nestihneš ani zareagovat a probodnou tě. Umíráš a nechápeš proč.")

                    #Stara chatka
                    if f == "stara chatka":
                        Atribut["Energie"] = 5
                        Atribut["Bezpečí"] = 5
                        print(Atribut)
                        print("\nPo příchodu k chatce slyšíš hlasy žoldáků. Otáčíš se na patě a běžíš tiše směrem k jeskyni, kde se schováváš. energie - 5")
                        Atribut[Bezpečí] = 0
                        print(Atribut)
                        print("Šli tě hledat a díky nízkému bezpečí tě našli a prodali do otroctví.\nKonec hry")

                    #Jeskyne - stat se kralem
                    if f == "jeskyne":
                        print(Atribut)
                        print("\nV jeskyni najdeš tajné doklady pro vstup na hrad a že ti náleží dědictví. ")
                        print("Jdeš na hrad a stáváš se králem")
                        print("VYHRÁL JSI HRU. \n1 konec hry Stát se králem.")

                # Rozděláš oheň
                if e == 2:
                    Atribut["Energie"] = 0
                    Atribut["Bezpečí"] = 5
                    Atribut["Zdraví"] = 40
                    Atribut["Teplo"] = 20
                    print(Atribut)
                    print("\nRozdělal jsi oheň a usnínáš. Energie -3 Bezpečí - 5 Teplo + 10. Napadl tě vlk. Zabil jsi jej harpunou. Zdraví -2%")
                    Atribut["Energie"] = 15
                    Atribut["Zdraví"] = 45
                    Atribut["Bezpečí"] = 10
                    print(Atribut)
                    print("\nPo vyhraném boji dospáváš. + 10 energie \nRozděláš oheň a opečeš rybu. + 5 zdraví + 5 energie + 5 bezpečí")
                    print("Kam se vydáš? Vyber si směr: \nchatka a cesta")
                    f = input()

                    #Chatka žoldnéřů
                    if f == "chatka":
                        Atribut["Energie"]= 10
                        print(Atribut)
                        print("\nNarážíš na žoldáky, tak potichu procházíš a jdeš nachystat pasti - 5 energie")
                        print("Čekáš schovaný na stromě a až se žoldácí chytí do pasti, jdeš si pro jejich hlavy.")
                        Atribut["Energie"] = 5
                        print("Pokračuješ dál po cestě k hradu. energie - 5 Ukazuješ získané hlavy. Vsichni oslavují, protože se jedná o zlé bandity.")
                        print("Stává se z tebe cenněný templář a žiješ si spokojený hojný život plný bojů a odměn.")
                        print("VYHRÁL JSI HRU!")

                    #Cesta
                    if f == "cesta":
                        Atribut["Energie"] = 0
                        print(Atribut)
                        print("Kráčíš si po cestě a vyhýbáš se nebezpečí. Vydíš konvoj plný bohatých lidí.")
                        print("Napadáš je? \nOdpověz ano nebo ne:")
                        g = input()

                        #Napadnout konvoj
                        if g == "ano":
                            Atribut["Energie"] = 5
                            print(Atribut)
                            print("Bez rozmyslu útočíš. energie- 10")
                            Atribut["Bezpečí"] = 0
                            Atribut["Zdraví"] = 10
                            print(Atribut)
                            print("Konvoj má dva strážce, kteří okamžitě reagují. Harpuna ti nepomohla a tak tě zajmou do vězení. - 10 bezpečí - 35 zdraví")
                            print("Máš 2 možnosti. Buďto se pokusíš utéct. Nebo odsedíš trest.")
                            print("Napiš utect nebo trest:")
                            h = input()

                            #Utéct z vězění
                            if h == "utect":
                                Atribut[Zdraví] = 0
                                print(Atribut)
                                print("Snažíš se nenápadně ukrást klíče hlídači.")
                                print("Stráž si toho všimne a hodí tě na obrátku. Umíráš oběšen před lidmi.")
                                print("Umřel jsi. \nKONEC HRY")

                            #Odsedět si trest.
                            if h == "trest":
                                print("Stráž tě nechává hladovět a často tě bije. Po 5 letech jsi propuštěn.")
                                print("Vyhýbáš se problémům. A žiješ jako vandrák.")
                                print("VUHRÁL JSI HRU")

                # Hledáš kryt a oheň
                # Usnout bez ohně.
                if e == 3:
                    Atribut["Energie"] = 0
                    Atribut["Bezpečí"] = 0
                    Atribut["Teplo"] = 0
                    print("Hledáš úkryt, ale nemáš dost sil. Usínáš po cestě. -3 energie -10 bezpečí")
                    print("Začíná ti být zima. -10 teplo Postupně umrzáš a vidíš, jak se na tebe šelmy sbíhají.")
                    print("Konec hry")

            #
            if d == 2:
                Atribut["Energie"] = 4
                Atribut["Teplo"] = 20
                Atribut["Bezpečí"] = 5
                print(Atribut)
                print("\nRozděláš oheň a jdeš spát. energie - 3 teplo + 10 bezpečí -5")
                print("Napádá tě vlk.")
                print("")

        # Vybiras obleceni.
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
                print("\nVenku mrzne. Triko a kraťasy nebyla nejlepší volba. Teplo -10, energie -3.")

            # Vzit si mikinu a kalhoty.
            elif d == 2:
                Atribut["Teplo"]= 25
                Atribut["Energie"]= 4
                print(Atribut)
                print("\nNení ti nejlépe. Teplo -5. Energie -3.")

            # Vzit si bundu a zateplene kalhoty.
            elif d == 3:
                Atribut["Teplo"]= 35
                Atribut["Energie"]= 4
                print(Atribut)
                print("\nIdeální možnost do tohoto počasí. Teplo + 5. Energie -3.")

            # Vzit si kozich.
            elif d == 4:
                Atribut["Teplo"]= 40
                Atribut["Energie"]= 2
                Atribut["Rychlost"]= 8
                print(Atribut)
                print("\nJe ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
            else:
                print("Zvolil jsi špatnou kombinaci")
        else:
            print("Zvolil jsi špatnou kombinaci")

    # Vybrat si obleceni.
    elif b == 2:
        Atribut["Energie"]= 12
        print(Atribut)
        print("\nJdeš se obléct. Co si vybereš?")
        print("1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
        c = input()
        c = int(c)

        # Oblect si triko a kratasy.
        if c == 1:
            Atribut["Teplo"]= 12
            print(Atribut)
            print("\nV triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")

        # Oblect si mikinu a kalhoty.
        elif c == 2:
            Atribut["Teplo"]= 15
            Atribut["Energie"]= 9
            print(Atribut)
            print("\nNení ti nejlépe. Teplo -5. Není ti nejlépe energie - 3")

        # Oblect si bundu a zateplene kalhoty.
        elif c == 3:
            Atribut["Teplo"]= 25
            Atribut["Energie"]= 12
            print(Atribut)
            print("\nIdeální možnost do tohoto počasí. Teplo + 5.")

        # Vzit si kozich
        elif c == 4:
            Atribut["Teplo"]= 40
            Atribut["Energie"]= 7
            Atribut["Rychlost"]= 8
            print(Atribut)
            print("\nJe ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
        else:
            print("Zvolil jsi špatnou kombinaci")

    # Jit ven.
    elif b == 3:
        Atribut["Teplo"]= 0
        Atribut["Zdraví"]= 0
        print(Atribut)
        print("\nZabouchli se za tebou dveře do krytu. Bez oblečení ses ocitl v mrazivém počasí. Do pár hodin umrzáš.")
        print("Konec hry \nZkus to znovu")
    else:
        print("Zvolil jsi špatnou kombinaci, zkus to znovu:")

    # Jdes si vybirat obleceni.
elif a == 2:
    Atribut["Zdraví"]= 40
    print(Atribut)
    print("\nOblékáš se a u toho nešíkovně shodíš sklenici s džusem do jídla, proto jsi hladový a žíznivý. -10 zdraví")
    print("Chceš tu kejdu zkusit sníst? Odpověď ano nebo ne")
    odpoved = input()

    # Snedl jsi kejdu
    if odpoved == "ano":
        Atribut["Zdraví"] = 30
        print(Atribut)
        print("\nUdělalo se ti strašně zle. Zdraví - 10")

        # Jdeš se obléct
        print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
        c = input()
        c = int(c)

        # Oblect si triko a kratasy.
        if c == 1:
            Atribut["Teplo"] = 10
            print(Atribut)
            print("\nV triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")

        # Oblect si mikinu a kalhoty.
        elif c == 2:
            Atribut["Teplo"] = 15
            Atribut["Energie"] = 7
            print(Atribut)
            print("\nNení ti nejlépe. Teplo -5. Není ti nejlépe energie - 3")

        # Oblect si bundu a zateplene kalhoty.
        elif c == 3:
            Atribut["Teplo"] = 15
            Atribut["Energie"] = 7
            print(Atribut)
            print("\nNení ti nejlépe. Teplo -5. Energie -3.")

        # Vzit si kozich
        elif c == 4:
            Atribut["Teplo"] = 30
            Atribut["Energie"] = 5
            Atribut["Rychlost"] = 8
            print(Atribut)
            print("\Je ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
        else:
            print("Zvolil jsi špatnou kombinaci.")

    elif odpoved == "ne":
        print("Nic se nestalo")

    #Jdeš se obléct
    print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
    c = input()
    c = int(c)

    # Oblect si triko a kratasy.
    if c == 1:
        Atribut["Teplo"] = 10
        print(Atribut)
        print("\nV triku je v mrazivém počasí zima. -10 teplo \nJe ti chladno, co uděláš. \nZvol číslo :")

    # Oblect si mikinu a kalhoty.
    elif c == 2:
        Atribut["Teplo"] = 15
        Atribut["Energie"] = 7
        print(Atribut)
        print("\nNení ti nejlépe. Teplo -5. Není ti nejlépe energie - 3")

    # Oblect si bundu a zateplene kalhoty.
    elif c == 3:
        Atribut["Teplo"] = 15
        Atribut["Energie"] = 7
        print(Atribut)
        print("\nNení ti nejlépe. Teplo -5. Energie -3.")

    # Vzit si kozich
    elif c == 4:
        Atribut["Teplo"] = 30
        Atribut["Energie"] = 5
        Atribut["Rychlost"] = 8
        print(Atribut)
        print("\nJe ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
    else:
        print("Zvolil jsi špatnou kombinaci.")

# Vyrazis ven.
elif a == 3:
    Atribut["Teplo"]= 0
    Atribut["Zdraví"]= 0
    print(Atribut)
    print("\nVyrážíš ven hladový a žíznivý. V mrazu nejsi schopný nic udělat. Navíc se za tebou zavřeli dveře do krytu. Umrzl jsi.")
    print("Konec hry \nZkus to znovu")

# Zustavas v krytu.
elif a == 4:
    Atribut["Teplo"]= 30
    Atribut["Zdraví"]= 40
    Atribut["Energie"]= 20
    print(Atribut)
    print("\nJdeš opět spát a trávíš čas v krytu. Odpočinul sis. Energie + 10. Objevil jsi i rukavice a čepici. Teplo + 10. Žiješ pokojně dokud nepřijde hlad a žízeň. Zdraví - 10. A ty musíš ven.")
    print("Co si oblečeš? \n1 Triko a kraťase \n2 Mikinu a kalhoty \n3 Bundu a zateplené kalhoty \n4 Kožich \nVyber opět číslem:")
    b = input()
    b = int(b)

    # Oblekas si triko a kratasy.
    if b == 1:
        Atribut["Energie"]= 17
        Atribut["Teplo"]= 20
        print(Atribut)
        print("\nV triku je v mrazivém počasí zima. -10 teplo, energie -3\nJe ti chladno, co uděláš. \nZvol číslo :")

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
        print("\nIdeální možnost do tohoto počasí. Teplo + 5. Energie -3.")

    # Oblekas si kozich.
    elif b == 4:
        Atribut["Teplo"]= 35
        Atribut["Energie"]= 17
        Atribut["Rychlost"]= 8
        print(Atribut)
        print("\nJe ti velmi teplo + 10, ale jsi pomalejší. Rychlost - 2. Hůř se plahočíš. Energie -5")
    else:
        print("Zvolil jsi špatnou kombinaci, zkus to znovu:")