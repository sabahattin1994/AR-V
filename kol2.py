from __future__ import division
#raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264
import time
import curses
import Adafruit_PCA9685
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
AIN1 = 35
AIN2 = 37
BIN1 = 38
BIN2 = 40
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT) 
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
pwm = Adafruit_PCA9685.PCA9685()

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
pwm.set_pwm_freq(60)
print('Moving servo on channel 0, press Ctrl-C to quit...')
a=520
b=600
c=390
d=357
e=630
f=465
g=208
def right():
    (GPIO.output(AIN1, GPIO.LOW))
    (GPIO.output(AIN2, GPIO.HIGH))
    (GPIO.output(BIN1, GPIO.LOW))
    (GPIO.output(BIN2, GPIO.HIGH))       
def left():
    (GPIO.output(AIN1, GPIO.HIGH))
    (GPIO.output(AIN2, GPIO.LOW))
    (GPIO.output(BIN1, GPIO.HIGH))
    (GPIO.output(BIN2, GPIO.LOW))
def forward():
    (GPIO.output(AIN1, GPIO.HIGH))
    (GPIO.output(AIN2, GPIO.LOW))
    (GPIO.output(BIN1, GPIO.LOW))
    (GPIO.output(BIN2, GPIO.HIGH))       
def reverse():
    (GPIO.output(AIN1, GPIO.LOW))
    (GPIO.output(AIN2, GPIO.HIGH))
    (GPIO.output(BIN1, GPIO.HIGH))
    (GPIO.output(BIN2, GPIO.LOW))
def off():
    (GPIO.output(AIN1, GPIO.LOW))
    (GPIO.output(AIN2, GPIO.LOW))
    (GPIO.output(BIN1, GPIO.LOW))
    (GPIO.output(BIN2, GPIO.LOW))
try:
    while True:
        char = screen.getch()
        if char == ord('t'):
            a=520
            b=600
            c=390
            d=392
            e=630
            f=465
            g=208
            pwm.set_pwm(0, 0, a)
            time.sleep(.5)
            pwm.set_pwm(1, 0, b)
            time.sleep(.5)
            pwm.set_pwm(2, 0, c)
            time.sleep(.5)
            pwm.set_pwm(3, 0, d)
            time.sleep(.5)            
            pwm.set_pwm(4, 0, e)
            time.sleep(.5)            
            pwm.set_pwm(5, 0, f)
            time.sleep(.5)            
            pwm.set_pwm(6, 0, g)
            time.sleep(.5)
            break
 ###########################################################       
	while char == ord('u'):
            forward()
            break
	while char == ord('j'):
	    reverse()
            break
	while char == ord('h'):
	    left()
            break
	while char == ord('k'):
	    right()
            break
	while  char != ord('u') and char != ord('j') and char != ord('h') and char != ord('k'):
	    off()
	    break
        ############################
        while char == ord('e') and g<=644:
            g=g+4
            pwm.set_pwm(6, 0, g)
            print ('g =', g)
            break

        while char == ord('r') and g>=204:
            g=g-4
            pwm.set_pwm(6, 0, g)
            print ('g =', g)
            break
        ############################
                
        while char == ord('f') and f<=650:
            f=f+5
            pwm.set_pwm(5, 0, f)
            print ('f =', f)
            break

        while char == ord('d') and f>=245:
            f=f-5
            pwm.set_pwm(5, 0, f)
            print ('f =', f)
            break
        ############################
                
        while char == ord('3') and e<=625:
            e=e+3
            pwm.set_pwm(4, 0, e)
            print ('e =', e)
            break

        while char == ord('4'):
            e=e-3
            pwm.set_pwm(4, 0, e)
            print ('e =', e)
            break
        ############################

        while char == ord('z') and d<=651:
            d=d+7
            pwm.set_pwm(3, 0, d)
            print ('d =', d)
            break

        while char == ord('x') and d>=131:
            d=d-7
            pwm.set_pwm(3, 0, d)
            print ('d =', d)
            break
        ############################
        while char == ord('a') and c<=650:
            c=c+5
            pwm.set_pwm(2, 0, c)
            print ('c =', c)
            break

        while char == ord('s') and c>=120:
            c=c-5
            pwm.set_pwm(2, 0, c)
            print ('c =', c)
            break
        ############################
        while char == ord('q') and b<=625:
            b=b+5
            pwm.set_pwm(1, 0, b)
            print ('b =', b)
            break

        while char == ord('w') and b>=225:
            b=b-5
            pwm.set_pwm(1, 0, b)
            print ('b =', b)
            break
        ############################
        while char == ord('1') and a<=620:
            a=a+5
            pwm.set_pwm(0, 0, a)
            print ('a =', a)
            break

        while char == ord('2') and a>=475:
            a=a-5
            pwm.set_pwm(0, 0, a)
            print ('a =', a)
            break                
    

            
finally:
    curses.nocbreak; screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    
                