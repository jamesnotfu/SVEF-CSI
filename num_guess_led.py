import board
import random
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05)
tries = 0

rv = False # set variable to true if guess is equal to secret

guess = int(input("Guess a number between 1 to 10: ")) 

secret = random.randint(1, 10)

while guess != secret:
    guess = int(input("Guess a number between 1 to 10: "))
    tries = tries + 1
    print("You have made " + str(tries) + " guess(es)")
    for i in range(len(pixels)):
        pixels[i] = (255, 0, 0)
        pixels.show()

if (guess == secret):
    rv = True;
    print("yea LESGO")

while True:
    if (rv):
        for i in range(len(pixels)):
            pixels[i] = (0, 255, 0)
            pixels.show()
        
######## some ideas for how you can improve your program #########

# 1. make a smiley face on success by disabling and enabling certain LEDS
# 2. show a rainbow/confetti upon guessing the right number
# 3. make the switch choose the "mode", e.g. a easy and hard mode where easy is 5 random numbers and hard is 10 random numbers
# 4. guess x amount of numbers in 10 times or display red -> you lost! :(=