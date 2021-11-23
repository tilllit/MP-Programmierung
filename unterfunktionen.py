# Importe:
import math



# Klasse für Line-Objekt erstellen
class Line:
    def __init__(self, X, Y, Z):
        self.g = None
        self.x = X
        self.y = Y
        self.z = Z
        self.i = ""
        self.j = ""

# Umformung in Integer
def convert_list_to_int(list):
    str = ""            # initialize String
    e = 0               # Für den Fall, dass String leer ist

    for x in list:      # add Elements to String
        str += x

    try:
        i = int(str)    # convert str to int
        return i        # return int

    except:
        return e        # return 0

# Umformung in Float
def convert_list_to_float(list):
    str = ""            # initialize String
    e = 0               # Für den Fall, dass String leer ist

    for x in list:      # add Elements to String
        str += x

    try:
        i = float(str)  # convert str to int
        return i        # return int
    except:
        return e        # return 0

# Punkt-Drehung
def rotate_point(p, angle):

    alpha = angle * (math.pi / 180)         # convert deg to rad

    p_n = [0, 0]                            # create array

    # calculation of new X & Y
    p_n[0] = (math.cos(alpha) * p[0]) \
             + (-math.sin(alpha) * p[1])
    p_n[1] = (math.sin(alpha) * p[0]) \
             + (math.cos(alpha) * p[1])

    p_n[0] = round(p_n[0], 3)               # runde X auf 3 Nachkommastellen
    p_n[1] = round(p_n[1], 3)               # runde Y auf 3 Nachkommastellen

    return p_n                              # return point

# Einheitsvektor Berechnen
def unit_vector(vec):
    bvec = math.sqrt((vec[0]**2) + (vec[1]**2))     # Betrag bilden
    try:
        X = vec[0] * (1 / bvec)
        Y = vec[1] * (1 / bvec)
        res = [X, Y]
    except:
        res = [0, 0]
    return res

# Berechnet den prozentualen Anteil
def cal_percent(vec):

    #   !!! --- EVTL UM DIRECTION ERWEITERN --- !!!

    p = [0, 0, 0]                                               # Erstellt Array
    p[0] = vec[0] * (-1) + vec[1] * 0                           # Berechnet v1
    p[1] = vec[0] * (0.5) + vec[1] * (-math.sqrt(3) / 2)        # Berechnet v2
    p[2] = vec[0] * (0.5) + vec[1] * (math.sqrt(3) / 2)         # Berechnet v3

    return p                                                    # giebt Array zurück

def convert_direction(perc):
    dir = [0, 0, 0]
    for i in range(len(perc)):
        if perc[i] < 0:                         # wenn negativ
            dir[i] = 1                          # direction auf 1
            perc[i] = math.sqrt(perc[i]**2)     # Betrag bilden

    return [perc, dir]                          # giebt percent und direction in 2-dimensionalem array zurück

# Berechnet die Anzahl der Schritte
def cal_steps(vec, perc, PPR, U):

    bvec = math.sqrt((vec[0] ** 2) + (vec[1] ** 2))     # Betrag des Vektors
    step = bvec * perc * (PPR / U)                      # Berechnet Schritte

    return step                                         # Giebt Anzahl der Schritte zurück