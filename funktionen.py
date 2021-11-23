import unterfunktionen
import math
import time
#import RPi.GPIO as GPIO

# ! ! !   E R W E I T E R U N G     N O T W E N D I G   ! ! !

# Liest N, X, Y & Z aus der Zeile und erstellt Line-Objekt
def laden(line):

    # Create variables
    l = list(line)
    c = 0
    G = ""
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
    L = unterfunktionen.Line(
                             unterfunktionen.convert_list_to_float(X),
                             unterfunktionen.convert_list_to_float(Y),
                             unterfunktionen.convert_list_to_float(Z)
                             )
    if G != "":
        L.g = unterfunktionen.convert_list_to_int(G)
    L.i = unterfunktionen.convert_list_to_float(I)
    L.j = unterfunktionen.convert_list_to_float(J)

    # returns Line-Object
    return L

def berechnung(line):

    #                   --- !!! K O N S T A N T E N !!! ---

    vE = 10                 # Einheitsgeschwindigkeit [m/s]     !--- VARIABEL ---!
    r = 0.051               # Radius omni wheel [m]
    PPR = 200               # Motor-Schritte pro Umdrehung
    U = 2 * math.pi * r     # Umfang des Rades



    # Hier sollen 3 Fälle unterschieden werden

    #       Fall 1: in der Line stehen nur X, Y oder Z Koordinaten -> einfach anfahren (mit Geschwindigkeit 1 [Bohren])

    #       Fall 2: G1 Befehl mit X, Y oder Z Koordinaten -> anfahren mit Geschwindigkeit 2 [Fräsen]

    #       Fall 3: G2 Befehl -> Zerstückelung in G1 Befehle -> abfahren mit Geschwindigkeit 2 [Fräsen]

    # Restliche Fälle / Lines sind vorerst uninteressant...     (G0 auch einprogrammieren???)


    # Fall 2:       --- G1 Befehl ---
    if line.g == 1:
        print("Berechnung für G1")

        EV = unterfunktionen.unit_vector([line.x, line.y])      # Einheitsvektor bilden
        perc = unterfunktionen.cal_percent(EV)                  # Prozentuale Anteile Berechnen

        #               --- !!! R I C H T U N G !!! ---

        perc, dir = unterfunktionen.convert_direction(perc)     # ruft convert_direction Funktion auf
        # gespeichert in dir (Array aus 3 Werten)


        #               --- !!! F R E Q U E N Z !!! ---

        freq = []                                               # Erstellt Array
        for i in range(len(perc)):
            freq.append((perc[i] * vE * PPR) / r)               # Berechnet die 3 Werte
        # gespeichert in vres (Array mit 3 Werten)


        #               --- !!! A N Z A H L  D E R  S C H R I T T E !!! ---

        step = []                                               # Erstellt Array
        for s in range(len(perc)):
            step.append(
                unterfunktionen.cal_steps(
                    [line.x, line.y], perc[s], PPR, U
                )
            )                                                   # Berechnet Schritte
        # gespeichert in step (Array mit 3 Werten)

        # Ende für G1 Befehl
        return [dir, freq, step]

    # Fall 3:       --- G2 Befehl ---
    if line.g == 2:

        #          !       F R A G E      !

        # In unserem beispel wird immer ein voller Halbkreis gefahren
        # wenn aber die Koordinate zu der gefahren werden soll (X, Y)
        # einen kleinerne oder größersn Winkel um den Mittelpunkt (I, J) fährt ? ! ? ! ? ! ? ! ? !

        # Annahme: Winel der um Mittelpunkt gefahren wird wird erstmal definiert...

        alpha = 180     # deg

        #           !       F R A G E       !

        # Und in wie viele Geraden unterteilt ? ! ? ! ? ! ? !
        # Annahme: Erstmal fester Wert

        pcs = 5         # Anzahl zerlegter Befehle

        beta = alpha / pcs
        koord = []
        for k in range(pcs-1):
            koord.append(unterfunktionen.rotate_point([line.x, line.y],(beta * (k+1))))

        #           !       F R A G E       !

        # koord ist ein Arrray und enthält pcs * X, Y Koordinaten entlang des Kreises
        # -> return koord ? ! ? ! ? !
        #   -> oder aufruf von hier
        #       -> dann return wert, der die ausführung dann aussetzt

        return [[1,2,3], [4,5,6], [7,8,9]]
    else:
        return False


def ausfuehren(data):

    if data != False:
        dir, freq, step = data
        print("Direction", dir)
        print("Frequency", freq)
        print("Steps", step)
        print("")
    else:
        print("G not defined")


    # Hier soll die Bewegung der Räder gesteuert werden

    # Eingangsparameter: Anzahl an Schritten, Freuquenz, Richtung (jeweils pro Motor)

        # GPIO.setmode(GPIO.BCM)
        #
        # # Laufzeit der PWMs berechen
        # t = ...
        #
        # #kofigurieren Direction Pins
        # GPIO.setup(Dir.pin.M0 , GPIOOUT)    #Direction.pin Motor 0
        #                     #Dir.pin Motor 1
        #                     #Dir.pin Motor 2
        #
        # #kofigurieren PWM Pins
        # GPIO.setup(PWM.pin.M0, GPIOOUT)     #PWM0.pin Motor 0
        #
        # #Starten der PWMs
        # PWM0 = GPIO.PWM( 'pin', 'Frequenz')
        # PWM0.start(50)
        # time.sleep(t)
        # PWM1.stop()