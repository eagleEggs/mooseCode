import RPi.GPIO as GPIO
import time
import sys
import asyncio

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

juxt = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--..",' ':" "}

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
        print("Issue with Argument Specifying Input File")
        print("Syntax: mooseCodeController.py textFile.txt")
        sys.exit()

    try:
        for row in open(sourceFile):
            print(row)
            for letter in row:
                try:
                    lowered = letter.lower()
                    convert = juxt[lowered]
                    await LEDout(convert)
                except:
                    print("Character not in Dictionary")
    except:
        print("Issue Opening Input File")


    finally:
        init.close()
        sys.exit()
        
try:
    init = asyncio.get_event_loop()
    init.run_until_complete(convertMoose())

finally:
    init.close()




