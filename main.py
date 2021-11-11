import funktionen


# Datei öffnen
file = open("gcode.txt","r")
lines = file.readlines()
file.close()

# Geht Zeile für Zeile durch
for line in lines:
    LineObj = funktionen.gcode(line)    # Schritt 1: G-Code
    print("Main: ", LineObj.nr,         # Print (überprüfen)
                    LineObj.x,
                    LineObj.y,
                    LineObj.z)
    funktionen.berechnung(LineObj)      # Schritt 2: Bewegung berechnen
