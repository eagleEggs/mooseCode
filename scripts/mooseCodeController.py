import RPi.GPIO as GPIO
import time
import sys
import asyncio

sourceFile = ' '

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

async def LEDout(letter):
    for symbol in letter:
        if symbol == ".":
            print(symbol)
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(27,GPIO.LOW)
            time.sleep(1)
        if symbol == "-":
            print(symbol)
            GPIO.output(27,GPIO.HIGH)
            time.sleep(3)
            GPIO.output(27,GPIO.LOW)
            time.sleep(1)
        if symbol == " ":
            print(symbol)
            GPIO.output(27,GPIO.LOW)
            time.sleep(7)


async def convertMoose():
    
    try:
        sourceFile = sys.argv[1]
    except:
        print("Issue with Input File Argument Syntax")
        sys.exit()

    try:
        for row in open(sourceFile):
            print(row)
            for letter in row:
                if letter == "a" or letter== "A":
                    letter = ".-"
                if letter == "b" or letter== "B":
                    letter = "-..."
                if letter == "c" or letter== "C":
                    letter = "-.-."
                if letter == "d" or letter== "D":
                    letter = "-.."
                if letter == "e" or letter== "E":
                    letter = "."
                if letter == "f" or letter== "F":
                    letter = "..-."
                if letter == "g" or letter== "G":
                    letter = "--."
                if letter == "h" or letter== "H":
                    letter = "...."
                if letter == "i" or letter== "I":
                    letter = ".."
                if letter == "j" or letter== "J":
                    letter = ".---"
                if letter == "k" or letter== "K":
                    letter = "-.-"
                if letter == "l" or letter== "L":
                    letter = ".-.."
                if letter == "m" or letter== "M":
                    letter = "--"
                if letter == "n" or letter== "N":
                    letter = "-."
                if letter == "o" or letter== "O":
                    letter = "---"
                if letter == "p" or letter== "P":
                    letter = ".--."
                if letter == "q" or letter== "Q":
                    letter = "--.-"
                if letter == "r" or letter== "R":
                    letter = ".-."
                if letter == "s" or letter== "S":
                    letter = "..."
                if letter == "t" or letter== "T":
                    letter = "-"
                if letter == "u" or letter== "U":
                    letter = "..-"
                if letter == "v" or letter== "V":
                    letter = "...-"
                if letter == "w" or letter== "W":
                    letter = ".--"
                if letter == "x" or letter== "X":
                    letter = "-..-"
                if letter == "y" or letter== "Y":
                    letter = "-.--"
                if letter == "z" or letter== "Z":
                    letter = "--.."
                if letter == " ":
                    letter = " "
                
                await LEDout(letter)


    finally:
        init.close()
        sys.exit()
        
try:
    init = asyncio.get_event_loop()
    init.run_until_complete(convertMoose())

finally:
    init.close()



