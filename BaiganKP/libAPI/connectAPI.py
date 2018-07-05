import RPi.GPIO as GPIO
import time
import requests


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
isPressed = "Button Not Pressed"


def pushToAPI():
    localTime = time.asctime( time.localtime(time.time()))
    r = requests.post('http://18.207.187.189:8080/v1/events', data = {'event': 'Button Accepted','timestamp': str(localTime)})
    return;

def pullFromAPI():
    #FIll in  get parameter with correct API key
    r = requests.get('http://18.207.187.189:8080/v1/pass_codes/ABCDEF')
    print r.text();
    return r;




    #while True:
    #input_state = GPIO.input(18)
    #if input_state == False:
    #   print('Button Pressed')
    #   isPressed = 'Button Pressed'
    #   localTime = time.asctime( time.localtime(time.time()))
    #   print('Local Time: ', localTime)
    #   time.sleep(0.2)
    #   print(r.text)


