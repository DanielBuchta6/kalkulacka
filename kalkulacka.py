x = input("Zadejte prvni cislo pro x:  ")
y = input("Zadejte druhe cislo pro y:  ")

x =int(x)
y = int(y)

print("pro sčítání zadejte +")
print("pro odčítání zadejte -")
print("pro násobení zadejte *")
print("pro dělení zadejte /")
print("pro mocnění zadejte **")
print("pro odmocnení zadejte /*")

znamenko = input("Zvolte operatora")



if znamenko == "+":
    vysledek = x+y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)
elif znamenko == "-":
    vysledek = x-y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)
elif znamenko == "*":
    vysledek = x*y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)   
elif znamenko == "/":
    if y != 0:
        vysledek = x/y
        vysledek = str(vysledek)
        print("vysledek je: " + vysledek)
    else:
        print("nemužeš dělit nulou")
elif znamenko == "**":
    vysledek = x**y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)
elif znamenko == "/*":
    vysledek = x /* y
    vysledek = str(vysledek)
    if y != 0:

    

