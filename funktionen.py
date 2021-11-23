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
    vE = 10                 # Einheitsgeschwindigkeit [m/s]     !--- VARIABEL ---!
    r = 0.051               # Radius omni wheel [m]
    PPR = 200               # Motor-Schritte pro Umdrehung
    U = 2 * math.pi * r     # Umfang des Rades

    # Motor Objekte erzeugen
    M1 = unterfunktionen.Motor(0, 0, 0)
    M2 = unterfunktionen.Motor(0, 0, 0)
    M3 = unterfunktionen.Motor(0, 0, 0)

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

        ret = unterfunktionen.convert_direction(perc)           # ruft convert_direction Funktion auf
        perc = ret[0]                                           # perc ist das erste Array
        dir = ret[1]                                            # dir ist das zweite Array
        # gespeichert in dir (Array aus 3 Werten)
        M1.dir = dir[0]

        #               --- !!! F R E Q U E N Z !!! ---

        vres = []
        for i in range(len(perc)):
            vres.append((perc[i] * vE * PPR) / r)
        # gespeichert in vres (Array mit 3 Werten)


        #               --- !!! A N Z A H L  D E R  S C H R I T T E !!! ---

        step = []
        for s in range(2):
            step.append(unterfunktionen.cal_steps([line.x, line.y], perc[s], PPR, U))
        # gespeichert in step (Array mit 3 Werten)




        # Ende für G1 Befehl
        return [dir, vres, step]


    # Fall 3:       --- G2 Befehl ---
    if line.g == 2:
        return 12
    else:
        return 12


def ausfuehren(data):
    if data == 12:
        print("Kein bekannte G-Befehl")
    else:
        dir = data[0]
        print("Ausführen dir: ", dir)


    # Hier soll die Bewegung der Räder gesteuert werden

    # Eingangsparameter: Anzahl an Schritten, Freuquenz, Richtung (jeweils pro Motor)

        GPIO.setmode(GPIO.BCM)

        # Laufzeit der PWMs berechen
        t = ...

        #kofigurieren Direction Pins
        GPIO.setup(Dir.pin.M0 , GPIOOUT)    #Direction.pin Motor 0
                            #Dir.pin Motor 1
                            #Dir.pin Motor 2

        #kofigurieren PWM Pins
        GPIO.setup(PWM.pin.M0, GPIOOUT)     #PWM0.pin Motor 0

        #Starten der PWMs
        PWM0 = GPIO.PWM( 'pin', 'Frequenz')
        PWM0.start(50)
        time.sleep(t)
        PWM1.stop()






    #
    pass