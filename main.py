import funktionen
import unterfunktionen

# Safe the G
G = ""
old_Line = unterfunktionen.Line(0, 0, 0)

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

    o_L = LineObj
    LineObj.x = LineObj.x - old_Line.x
    LineObj.y = LineObj.y - old_Line.y
    LineObj.z = LineObj.z - old_Line.z
    old_Line = o_L

    data = funktionen.berechnung(LineObj)   # Schritt 2: Bewegung berechnen
    funktionen.ausfuehren(data)             # Schritt 3: Bewegung ausführen



#                 !!!   ----    ! TESTBEREICH !     ----   !!!

    if LineObj.g != None:
        print("G", LineObj.g, "Befehl")       # testet .g attribut eines Line Objektes