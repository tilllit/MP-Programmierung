import funktionen

# test mooooooooooooo
x=1 #test

#test222

# Datei öffnen
file = open("gcode.txt","r")
lines = file.readlines()
file.close()

# Geht Zeile für Zeile durch
for line in lines:
    LineObj = funktionen.laden(line)    # Schritt 1: G-Code
    print("Laden in Main: ", LineObj.nr,         # Print (überprüfen)
                    LineObj.x,
                    LineObj.y,
                    LineObj.z)
    funktionen.berechnung(LineObj)      # Schritt 2: Bewegung berechnen
    funktionen.ausfuehren()             # Schritt 3: Bewegung ausführen
