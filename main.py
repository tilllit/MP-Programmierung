import funktionen
import unterfunktionen

# Safe attributes
old = unterfunktionen.Line()
old.reset_ko()

# Open File
file = open("gcode-3.txt", "r")
lines = file.readlines()
file.close()

# Geht Zeile nach Zeile durch
for line in lines:
    LineObj = funktionen.laden(line)        # Schritt 1: G-Code

    # Carrying the G - command
    if LineObj.g is not None:
        old.g = LineObj.g
    elif LineObj.x != 0 or LineObj.y != 0 or LineObj.z != 0:
        LineObj.g = old.g

    # Carrying old position
    if LineObj.x is not None:
        carry = old.x
        old.x = LineObj.x
        LineObj.x = LineObj.x - carry
    if LineObj.y is not None:
        carry = old.y
        old.y = LineObj.y
        LineObj.y = LineObj.y - carry
    if LineObj.z is not None:
        carry = old.z
        old.z = LineObj.z
        LineObj.z = LineObj.z - carry


    data = funktionen.berechnung(LineObj)   # Schritt 2: Bewegung berechnen
    funktionen.ausfuehren(data)             # Schritt 3: Bewegung ausfuehren



#                 !!!   ----    ! TESTBEREICH !     ----   !!!

    if LineObj.g is not None:
        print("G", LineObj.g, "Befehl")       # testet .g attribut eines Line Objektes
