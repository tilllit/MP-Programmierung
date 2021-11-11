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