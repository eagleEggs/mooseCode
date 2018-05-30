import RPi.GPIO as GPIO
import time
import sys
import asyncio

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

juxt = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--..",' ':" ",'A':".-",'B':"-...",'C':"-.-.",'D':"-..",'E':".",'F':"..-.",'G':"--.",'H':"....",'I':"..",'J':".---",'K':"-.-",'L':".-..",'M':"--",'N':"-.",'O':"---",'P':".--.",'Q':"--.-",'R':".-.",'S':"...",'T':"-",'U':"..-",'V':"...-",'W':".--",'X':"-..-",'Y':"-.--",'Z':"--.."}

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
        print("Issue with Argument")
        sys.exit()

    try:
        for row in open(sourceFile):
            print(row)
            for letter in row:
                try:
                    convert = juxt[letter]
                    await LEDout(convert)
                except:
                    print("Unknown Entry")


    finally:
        init.close()
        sys.exit()
        
try:
    init = asyncio.get_event_loop()
    init.run_until_complete(convertMoose())

finally:
    init.close()




