import funktionen
import unterfunktionen

# Datei öffnen
file = open("gcode-2.txt","r")
lines = file.readlines()
file.close()

# Geht Zeile für Zeile durch
for line in lines:
    LineObj = funktionen.laden(line)        # Schritt 1: G-Code
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