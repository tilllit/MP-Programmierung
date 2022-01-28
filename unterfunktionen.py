# Importe:
import math


# Klasse für Line-Objekt erstellen
class Line:
    def __init__(self):
        self.g = None
        self.x = None
        self.y = None
        self.z = None

    def reset_ko(self):
        self.x = 0
        self.y = 0
        self.z = 0

# Umformung in Integer
def convert_list_to_int(list):
    str = ""            # initialize String

    for x in list:      # add Elements to String
        str += x

    try:
        i = int(str)    # convert str to int
        return i        # return int

    except:
        return False    # return fals

# Umformung in Float
def convert_list_to_float(list):
    str = ""            # initialize String

    for x in list:      # add Elements to String
        str += x

    try:
        i = float(str)  # convert str to int
        return i        # return int
    except:
        return False    # return false

# Einheitsvektor Berechnen
def unit_vector(vec):
    if vec[0] == None:
        vec[0] = 0
    if vec[1] == None:
        vec[1] = 0
    bvec = math.sqrt((vec[0]**2) + (vec[1]**2))     # Betrag bilden
    try:
        X = vec[0] * (1 / bvec)
        Y = vec[1] * (1 / bvec)
        res = [X, Y]
    except:
        res = [0, 0]
    return res

# Ermittelt Richtung und bildet den Betrag der prozentualen Anteile
def convert_direction(perc):
    dir = [0, 0, 0]
    for i in range(len(perc)):
        if perc[i] < 0:                         # wenn negativ
            dir[i] = 1                          # direction auf 1
            perc[i] = math.sqrt(perc[i]**2)     # Betrag bilden

    return [perc, dir]                          # giebt percent und direction in 2-dimensionalem array zurueck

# Berechnet die Dauer gesamt
def cal_time(vec, vE):
    if vec[0] == None:
        vec[0] = 0
    if vec[1] == None:
        vec[1] = 0
    bvec = math.sqrt((vec[0] ** 2) + (vec[1] ** 2))  # Betrag des Vektors
    time = bvec / (vE * 1000)                        # Berechnung der Dauer [mm/(m/s * 1000)]
    time = time * 1.28                               # Adjustment Factor

    return time                                      # Giebt die Dauer zurueck in sec

# Berechnet den prozentualen Anteil
def cal_percent(vec):

    #   !!! --- EVTL UM DIRECTION ERWEITERN --- !!!

    p = [0, 0, 0]                                               # Erstellt Array
    p[0] = vec[0] * (-1) + vec[1] * 0                           # Berechnet v1
    p[1] = vec[0] * (0.5) + vec[1] * (-math.sqrt(3) / 2)        # Berechnet v2
    p[2] = vec[0] * (0.5) + vec[1] * (math.sqrt(3) / 2)         # Berechnet v3

    return p                                                    # giebt Array zurueck

#           --- !!! F U N C  F O R  Z !!! ---

def cal_z_time(vZ, Z):
    dir = 0
    if Z == None:
        Z = 0
    if Z < 0:
        dir = 1
        Z = math.sqrt(Z **2)
    tim = (Z / vZ) * 10

    return [tim, dir]
