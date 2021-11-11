import funktionen


# Datei öffnen
file = open("gcode.txt","r")
lines = file.readlines()
file.close()

# Geht Zeile für Zeile durch
for line in lines:
    LineObj = funktionen.gcode(line)
    print("Main: ", LineObj.nr, LineObj.x,LineObj.y, LineObj.z)
    funktionen.berechnung(LineObj)