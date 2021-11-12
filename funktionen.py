import unterfunktionen
import math

# ! ! !   E R W E I T E R U N G     N O T W E N D I G   ! ! !

# Liest N, X, Y & Z aus der Zeile und erstellt Line-Objekt
def laden(line):

    # Create variables
    l = list(line)
    c = 0
    N = ""
    X = ""
    Y = ""
    Z = ""

    # Read the Line (Hier weitere G-Befehle hinzufügen!!!!)
    for x in l:
        if (x == "N"):
            c2 = c + 1
            while (l[c2] != " "):
                N += l[c2]
                c2 += 1
        if (x == "X"):
            c2 = c + 1
            try:
                while (l[c2] != " "):
                    X += l[c2]
                    c2 += 1
            except:
                break
        if (x == "Y"):
            c2 = c + 1
            try:
                while (l[c2] != " "):
                    Y += l[c2]
                    c2 += 1
            except:
                break
        if (x == "Z"):
            c2 = c + 1
            try:
                while (l[c2] != " "):
                    Z += l[c2]
                    c2 += 1
            except:
                break
        c += 1

    # Create Line-Object with converted numbers
    L = unterfunktionen.Line(unterfunktionen.convert_list_to_int(N),
                             unterfunktionen.convert_list_to_float(X),
                             unterfunktionen.convert_list_to_float(Y),
                             unterfunktionen.convert_list_to_float(Z)
                             )

    # returns Line-Object
    return L

def berechnung(line):
    print("Hier wird die Berechnung", line.nr,"der Rädergeschw. stattfinden!")
    X = line.x
    if (X != 0):
        print("X für Vektor")
    else:
        print("Kein X")
    y =line.y
    if (y != 0):
        print("y für Vektor")
    else:{print("Kein y")}

    # Berechnung der Rototationsgeschwindigkeiten
    Vx = line.x
    Vy = line.y
    p1 = Vx * (-1) + Vy * 0
    p2 = Vx * (0.5) + Vy * (-math.sqrt(3) / 2)
    p3 = Vx * (0.5) + Vy * (math.sqrt(3) / 2)
    print(p1, p2, p3)


def ausfuehren():
    print("Ausführen aufgerufen")
    # no no nonsense BULLLshit