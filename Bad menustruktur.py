#Dette er et dårlig strukuteret program, hvis man skal bruge en menu i sit Pythonprogram

print("1) menu 1")
print("2) menu 2")
print("3) menu 3")
print("4) stop program")


Menunr=int(input("Vælg menu nr."))
wh=1

while wh==1:
    if Menunr == 1:
        # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt menu nr. 1")
        print("1) menu 1")
        print("2) menu 2")
        print("3) menu 3")
        print("4) stop program")
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 2:
         # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt menu nr. 2")
        print("1) menu 1")
        print("2) menu 2")
        print("3) menu 3")
        print("4) stop program")
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 3:
         # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt menu nr. 3")
        print("1) menu 1")
        print("2) menu 2")
        print("3) menu 3")
        print("4) stop program")
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 4:
        print("Nu stopper programmet!!!")
        wh=2
