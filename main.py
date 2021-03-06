import funktionen
import unterfunktionen
from gpiozero import Button, LED
from signal import pause

ledg = LED(18)
ledr = LED(23)

def main():
    ledg.on()
    ledr.off()
    start_button = Button(2)
    up_button = Button(3)
    down_button = Button(4)
    
    start_button.when_pressed = start
    up_button.when_pressed = Z_up
    down_button.when_pressed = Z_down
    
    pause()

def start():
    
    ledg.off()
    ledr.on()
    
    # Safe attributes
    old = unterfunktionen.Line()
    old.reset_ko()

    # Open File
    file = open("/media/usb/MP/gcode.txt", "r")

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
    
    ledr.off()
    ledg.on()

def Z_up():
    
    ledg.off()
    ledr.on()
    
    vZ = 2  # Z - Geschwindigkeit [mm/s]
    Z_PPR = 200  # Motor-Schritte pro Umdrehung
    LPR = 9.6  # Hubweg pro Umdrehung [mm]
    Z = 2  # Fahrweg Einheit [mm]
    z_freq = vZ / (LPR / Z_PPR)
    z_tim, z_dir = unterfunktionen.cal_z_time(vZ, Z)
    arr = [z_freq, z_tim, 0]
    funktionen.ausfuehren([[0, 0, 0], [0, 0, 0], 0, arr])
    
    ledr.off()
    ledg.on()

def Z_down():
    
    ledg.off()
    ledr.on()
    
    vZ = 2          # Z - Geschwindigkeit [mm/s]
    Z_PPR = 200     # Motor-Schritte pro Umdrehung
    LPR = 9.6       # Hubweg pro Umdrehung [mm]
    Z = 2           # Fahrweg Einheit [mm]
    z_freq = vZ / (LPR / Z_PPR)
    z_tim, z_dir = unterfunktionen.cal_z_time(vZ, Z)
    arr = [z_freq, z_tim, 1]
    funktionen.ausfuehren([[0, 0, 0], [0, 0, 0], 0, arr])
    
    ledr.off()
    ledg.on()

if __name__ == '__main__':
    main()
