
import datetime
import requests
import json


class apiConnect:
    
    def pushToAPI(self, valOfCode):
        timeNow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print(timeNow)
        r = requests.post("http://18.207.187.189:8080/v1/pass_codes", json={"product_id": "testingBox1","pass_code": str(valOfCode),"created_ts": str(timeNow)})
        print (r.text)
        return 

    def pullFromAPI(self):
    #FIll in  get parameter with correct API key
        rs = requests.get('http://18.207.187.189:8080/v1/pass_codes/testingBox1')
        data = rs.json()
        json_str = json.dumps(data)
        resp = json.loads(json_str)
        return resp['pass_code']
    




    #while True:
    #input_state = GPIO.input(18)
    #if input_state == False:
    #   print('Button Pressed')
    #   isPressed = 'Button Pressed'
    #   localTime = time.asctime( time.localtime(time.time()))
    #   print('Local Time: ', localTime)
    #   time.sleep(0.2)
    #   print(r.text)


