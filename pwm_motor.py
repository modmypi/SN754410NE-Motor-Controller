import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

M1_F = 17
M1_B = 18
M2_F = 22
M2_B = 23

GPIO.setup(M1_F, GPIO.OUT)
GPIO.setup(M1_B, GPIO.OUT)
GPIO.setup(M2_F, GPIO.OUT)
GPIO.setup(M2_B, GPIO.OUT)

m1f = GPIO.PWM(M1_F, 200)
m1b = GPIO.PWM(M1_B, 200)
m2f = GPIO.PWM(M2_F, 200)
m2b = GPIO.PWM(M2_B, 200)

try:
    while True:
        print "Forward 50%"
        m1f.start(50)
        m2f.start(50)
        sleep(2)
        print "Forward 100%"
        m1f.ChangeDutyCycle(100)
        m2f.ChangeDutyCycle(100)
        sleep(2)
        print "Stop"
        m1f.stop()
        m2f.stop()
        sleep(1)
        print "Backward 50%"
        m1b.start(50)
        m2b.start(50)
        sleep(2)
        print "Backwards 100%"
        m1b.ChangeDutyCycle(100)
        m2b.ChangeDutyCycle(100)
        sleep(2)
        print "M1 Stop"
        m1b.stop()
        m2b.stop()
        sleep(1)
except:
    GPIO.cleanup()
