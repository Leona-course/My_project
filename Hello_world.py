Rychlost = 10
Zdraví = 50
Teplo = 20
Bezpečí = 10
Energie = 10
Atribut = [Rychlost, Zdraví, Teplo, Bezpečí, Energie]
print(Atribut[2])


a = """
Tady neco muzu napsat
a tady
taky
"""

print(a)

b = 'Hello world'

print(b)


nwm = "tady neco napisu \ntady bude druhy radek"

print(nwm)

nwm2 = "tady neco napisu \\ntady bude druhy radek"

print(nwm2)

zkouska = "blabla \"neco rekl\""
print(zkouska)

def add(prvni, druhe):
    return prvni+druhe



a = add(2, 5) == 8
if a:
    print(a)
else:
    print("neumis pocitat")
