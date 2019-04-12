#Dette er et program til bygge videre på, hvis man skal bruge en menu i sit Pythonprogram
def prmenu():
    print("1) menu 1")
    print("2) menu 2")
    print("3) menu 3")
    print("4) stop program")

prmenu()
Menunr=int(input("Vælg menu nr."))
wh=1

while wh==1:
    if Menunr == 1:
        # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt menu nr. 1")
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 2:
         # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt menu nr. 2")
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 3:
         # Her skal det kode sættes ind som skal udføre et eller andet
        print("du har valgt menu nr. 3")
        prmenu()
        Menunr=int(input("Vælg menu nr."))

    if Menunr == 4:
        print("Nu stopper programmet!!!")
        wh=2

