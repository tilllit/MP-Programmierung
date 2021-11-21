# Importe:
import math

# Klasse für Line-Objekt erstellen
class Line:
    def __init__(self, Nr, X, Y, Z):
        self.nr = Nr
        self.x = X
        self.y = Y
        self.z = Z

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
