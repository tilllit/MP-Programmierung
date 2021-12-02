import unterfunktionen
import math
import time
import RPi.GPIO as GPIO

# ! ! !   E R W E I T E R U N G     N O T W E N D I G   ! ! !

# Liest G, X, Y & Z aus der Zeile und erstellt Line-Objekt
def laden(line):

    # Create variables
    l = list(line)
    c = 0
    G = ""
    X = ""
    Y = ""
    Z = ""

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
        c += 1

    # Create Line-Object with converted numbers
    L = unterfunktionen.Line(
                             unterfunktionen.convert_list_to_float(X),
                             unterfunktionen.convert_list_to_float(Y),
                             unterfunktionen.convert_list_to_float(Z)
                             )
    if G != "":
        L.g = unterfunktionen.convert_list_to_int(G)

    # returns Line-Object
    return L

def berechnung(line):

    #                   --- !!! K O N S T A N T E N (Killough) !!! ---

    vE = 0.005              # Einheitsgeschwindigkeit [m/s]     !--- VARIABEL ---!
    r = 0.051               # Radius omni wheel [m]
    PPR = 200               # Motor-Schritte pro Umdrehung
    U = 2 * math.pi * r     # Umfang des Rades

    #                   --- !!! Z - A C H S E (Settings) !!! ---

    vZ = 0.005              # Z - Geschwindigkeit [m/s]
    Z_PPR = 200             # Motor-Schritte pro Umdrehung
    LPR = 3                 # Hubweg pro Umdrehung [mm]


    #                   --- G1  B E F E H L ---
    if line.g == 1:
        print("Berechnung fuer G1")

        #       --- !!! Z - B E R E C H N U N G !!! ---

        if line.z != 0:
            zfreq = 0 # ???
            pass

        #       --- !!! K I L L O U G H  B E R E C H N U N G !!! ---

        EV = unterfunktionen.unit_vector([line.x, line.y])      # Einheitsvektor bilden
        perc = unterfunktionen.cal_percent(EV)                  # Prozentuale Anteile Berechnen

        #               --- !!! R I C H T U N G !!! ---

        perc, dir = unterfunktionen.convert_direction(perc)     # ruft convert_direction Funktion auf
        # gespeichert in dir (Array aus 3 Werten)


        #               --- !!! F R E Q U E N Z !!! ---

        freq = []
        for i in range(len(perc)):
            freq.append((perc[i] * vE * PPR) / r)
        # gespeichert in freq (Array mit 3 Werten)


        #               --- !!! D A U E R !!! ---

        #tim = []                                                                   # 3 Dauern berechnen
        #for s in range(len(perc)):
            #tim.append(unterfunktionen.cal_tim([line.x, line.y], perc[s], vE))

        tim = unterfunktionen.cal_time([line.x, line.y], vE)                        # Eine Dauer berechnen
        # gespeichert in tim (Array mit 3 Werten)


        # Ende für G1 Befehl
        return [dir, freq, tim]


    else:
        return False

def ausfuehren(data):

    if data != False:
        dir, freq, tim = data
        print("Direction", dir)
        print("Frequency", freq)
        print("Time", tim)
        print("")

        f0, f1, f2 = freq           # Weist die Frequenzen zu

        GPIO.setmode(GPIO.BCM)      # Definiert das Nummerierung "GPIOx" für Pin Bezeichnung verwendet wird

        #Ausgangspins konfigurieren

        #             --- Konfigurieren Direction Pins ---
        GPIO.setup(10, GPIO.OUT)       #Dir.pin Motor 0
        GPIO.setup(9 , GPIO.OUT)       #Dir.pin Motor 1
        GPIO.setup(11, GPIO.OUT)       #Dir.pin Motor 2

        #             --- Konfigurieren PWM Pins ---
        PWM0 = GPIO.setup(17, GPIO.OUT) #PWM0.pin Motor 0
        PWM1 = GPIO.setup(27, GPIO.OUT) #PWM1.pin Motor 1
        PWM2 = GPIO.setup(22, GPIO.OUT) #pwm2.pin Motor 2

        run = []                       # Array zum vermeiden von try & except

        #             --- Übergeben der berechneten Frequenzen ---
        if f0 != 0:
            PWM0 = GPIO.PWM( 17, f0)   # Konfigurieren der PWM0 für MOTOR 0 mit GPIO.PWM('Pin','Frequenz')
            run.append(PWM0)
        if f1 != 0:
            PWM1 = GPIO.PWM( 27, f1)   # Konfigurieren der PWM1 für MOTOR 1 mit GPIO.PWM('Pin','Frequenz')
            run.append(PWM1)
        if f2 != 0:
            PWM2 = GPIO.PWM( 22, f2)   # Konfigurieren der PWM2 für MOTOR 2 mit GPIO.PWM('Pin','Frequenz')
            run.append(PWM2)

        #              --- Übergeben und setzen der  Richtungen (DIR.Pin 1=HIGH=>CCW /DIR.Pin 0=LOW=>CW)---

        dir_pins = [10, 9, 11]
        for i in range(len(dir)):
            if dir[i] == 0:
                GPIO.output(dir_pins[i], GPIO.LOW)
            if dir[i] == 1:
                GPIO.output(dir_pins[i], GPIO.HIGH)

        #             --- Starten der PWMs ---

        for r in run:
            r.start(50)

        # sonst halt mit einzelnen if-Abfragen...

        #              --- Fahrdauer ---
        time.sleep(tim)

        #              --- Stoppen der PWMs ---

        for r in run:
            r.stop()

    else:
        print("G not defined")