print("Jsi venku, kde sněží, přemýšlíš co uděláš dále.")
print("1 Najdeš vodu.")
print("2 Vytvoříš pasti.")
print("Najdeš skrýš, kde přespíš a uděláš oheň.")
Zacatek = MoznostA
print(MoznostD)
print("Vyber číslo:")
a = input()
a = int(a)


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