print("Jsi venku, kde sněží, přemýšlíš co uděláš dále.")
print("1 Najdeš vodu.")
print("2 Vytvoříš pasti.")
print("Najdeš skrýš, kde přespíš a uděláš oheň.")
Zacatek = MoznostA
print(MoznostD)
print("Vyber číslo:")
a = input()
a = int(a)


print("Chceš tu kejdu zkusit sníst? Odpověď ano nebo ne")
    odpoved = input()
    if odpoved == "ano":
        thisdict["Zdraví"]= 30
        print(thisdict)
        print("Udělalo se ti strašně zle. Zdraví - 10")
    elif odpoved == "ne":
        print("Nic se nestalo")