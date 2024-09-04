import RPi.GPIO as GPIO
import time
import copy

GPIO.setmode(GPIO.BOARD)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.output(5, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(23, GPIO.LOW)

GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0


while True:
    if GPIO.input(3) == GPIO.HIGH:
        count += 1
        if count > 8:
            count = 0

        print(count)

        fake = copy.deepcopy(count)

        if fake == 8:
            GPIO.output(23, GPIO.HIGH)
            fake -= 8
        else:
            GPIO.output(23, GPIO.LOW)
        if fake >= 4:
            GPIO.output(21, GPIO.HIGH)
            fake -= 4
        else:
            GPIO.output(23, GPIO.LOW)
        if fake >= 2:
            GPIO.output(19, GPIO.HIGH)
            fake -= 2
        else:
            GPIO.output(23, GPIO.LOW)
        if fake >= 1:
            GPIO.output(5, GPIO.HIGH)
            fake -= 1
        else:
            GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)