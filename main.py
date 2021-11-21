import funktionen
import unterfunktionen

# Datei öffnen
file = open("gcode.txt","r")
lines = file.readlines()
file.close()

# Geht Zeile für Zeile durch
for line in lines:
    LineObj = funktionen.laden(line)    # Schritt 1: G-Code
    funktionen.berechnung(LineObj)      # Schritt 2: Bewegung berechnen
    funktionen.ausfuehren()             # Schritt 3: Bewegung ausführen

                 !!!   ----    ! TESTBEREICH !     ----   !!!

    if LineObj.g != 0:
        print("G test:", LineObj.g)       # testet .g attribut eines Line Objektes


# Test "rotate_point" Funktion
print("Rotate Point", unterfunktionen.rotate_point([0, 5], 180))
print("Einheitsvektorfunktion: ", unterfunktionen.unit_vector([3, 5]))