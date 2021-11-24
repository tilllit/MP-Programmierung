import funktionen
import unterfunktionen

# Safe the G
G = ""

# Datei öffnen
file = open("gcode-3.txt","r")
lines = file.readlines()
file.close()

# Geht Zeile für Zeile durch
for line in lines:
    LineObj = funktionen.laden(line)        # Schritt 1: G-Code

    if LineObj.g != None:
        G = LineObj.g
    elif LineObj.x != 0 or LineObj.y != 0 or LineObj.z != 0:
        LineObj.g = G

    data = funktionen.berechnung(LineObj)   # Schritt 2: Bewegung berechnen
    funktionen.ausfuehren(data)             # Schritt 3: Bewegung ausführen



#                 !!!   ----    ! TESTBEREICH !     ----   !!!

    if LineObj.g != None:
        print("G", LineObj.g, "Befehl")       # testet .g attribut eines Line Objektes
        print("")




#               !!!     ---     ! WEITERE TESTS !       ---     !!!
print("")
print("Rotate Point", unterfunktionen.rotate_point([0, 5], 180))
print("Einheitsvektorfunktion: ", unterfunktionen.unit_vector([3, 5]))