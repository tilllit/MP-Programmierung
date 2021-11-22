import unterfunktionen
import math

# ! ! !   E R W E I T E R U N G     N O T W E N D I G   ! ! !

# Liest N, X, Y & Z aus der Zeile und erstellt Line-Objekt
def laden(line):

    # Create variables
    l = list(line)
    c = 0
    G = ""
    N = ""
    X = ""
    Y = ""
    Z = ""
    I = ""
    J = ""

    # Read the Line (Hier weitere G-Befehle hinzufügen!!!!)
    for x in l:
        if (x == "G"):                  # Abfrage welcher G-Befehl
            c2 = c + 1
            try:
                while (l[c2] != " "):
                    G += l[c2]
                    c2 += 1
            except:
                break
        if (x == "N"):                  # evtl. unnötig -> Je nach Postprozessor...
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
        if (x == "I"):
            c2 = c + 1
            try:
                while (l[c2] != " "):
                    I += l[c2]
                    c2 += 1
            except:
                break
        if (x == "J"):
            c2 = c + 1
            try:
                while (l[c2] != " "):
                    J += l[c2]
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
    L.g = unterfunktionen.convert_list_to_int(G)
    L.i = unterfunktionen.convert_list_to_float(I)
    L.j = unterfunktionen.convert_list_to_float(J)

    # returns Line-Object
    return L

def berechnung(line):

    # Definition of constants
    vE = 10     # Einheitsgeschwindigkeit [m/s]     !--- VARIABEL ---!
    r = 0.1     # Radius omni wheel [m]
    PPR = 200   # Motor-Schritte pro Umdrehung

    # Hier sollen 3 Fälle unterschieden werden

    #       Fall 1: in der Line stehen nur X, Y oder Z Koordinaten -> einfach anfahren (mit Geschwindigkeit 1 [Bohren])

    #       Fall 2: G1 Befehl mit X, Y oder Z Koordinaten -> anfahren mit Geschwindigkeit 2 [Fräsen]

    #       Fall 3: G2 Befehl -> Zerstückelung in G1 Befehle -> abfahren mit Geschwindigkeit 2 [Fräsen]

    # Restliche Fälle / Lines sind vorerst uninteressant...     (G0 auch einprogrammieren???)

    # Fall 2:       --- G1 Befehl ---
    if line.g == 1:
        print("Berechnung für G1")

        EV = unterfunktionen.unit_vector([line.x, line.y])       # Einheitsvektor bilden
        Vx = EV[0]
        Vy = EV[1]

        # Prozentuale Anteile Berechnen (evtl. als Unterfunktion auslagern!!!)
        p = [0, 0, 0]
        p[0] = Vx * (-1) + Vy * 0
        p[1] = Vx * (0.5) + Vy * (-math.sqrt(3) / 2)
        p[2] = Vx * (0.5) + Vy * (math.sqrt(3) / 2)

        vres = []
        for i in range(len(p)):
            vres.append((p[i] * vE * PPR) / r)
        print("Vres: ", vres)

        # Berechnung der Dauer ...

    # Fall 3:       --- G2 Befehl ---
    if line.g == 2:
        pass


def ausfuehren():

    # Hier soll die Bewegung der Räder gesteuert werden

    # PWM konfigurieren und betreiben...

    # no no nonsense BULLLshit
    pass