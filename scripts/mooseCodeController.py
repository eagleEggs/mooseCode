import RPi.GPIO as GPIO
import time
import sys

sourceFile = ''

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

def LEDout(letter):
    for symbol in letter:
        time.sleep(3)
        if symbol == ".":
            print(symbol)
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(27,GPIO.LOW)
        if symbol == "-":
            print(symbol)
            GPIO.output(27,GPIO.HIGH)
            time.sleep(3)
            GPIO.output(27,GPIO.LOW)
        if symbol == " ":
            print(symbol)
            GPIO.output(27,GPIO.LOW)
            time.sleep(7)
        

def convertMoose():

    try:
        sourceFile = sys.argv[1]
    except:
        print("Issue with Argument")
        sys.exit()
    try:
        for row in open(sourceFile):
            print(row)
            for letter in row:
                if letter == "a":
                    letter = ".-"
                if letter == "b":
                    letter = "-..."
                if letter == "c":
                    letter = "-.-."
                if letter == "d":
                    letter = "-.."
                if letter == "e":
                    letter = "."
                if letter == "f":
                    letter = "..-."
                if letter == "g":
                    letter = "--."
                if letter == "h":
                    letter = "...."
                if letter == "i":
                    letter = ".."
                if letter == "j":
                    letter = ".---"
                if letter == "k":
                    letter = "-.-"
                if letter == "l":
                    letter = ".-.."
                if letter == "m":
                    letter = "--"
                if letter == "n":
                    letter = "-."
                if letter == "o":
                    letter = "---"
                if letter == "p":
                    letter = ".--."
                if letter == "q":
                    letter = "--.-"
                if letter == "r":
                    letter = ".-."
                if letter == "s":
                    letter = "..."
                if letter == "t":
                    letter = "-"
                if letter == "u":
                    letter = "..-"
                if letter == "v":
                    letter = "...-"
                if letter == "w":
                    letter = ".--"
                if letter == "x":
                    letter = "-..-"
                if letter == "y":
                    letter = "-.--"
                if letter == "z":
                    letter = "--.."
                if letter == " ":
                    letter = " "
                LEDout(letter)


    finally:
        sys.exit()
        
        
convertMoose()
