import termux
import cv2
import requests
import sys
import time

if __name__ == '__main__':
    cam_ip = sys.argv[1]
    api_server_url = sys.argv[2]

cam_path= 'http://192.168.1.' + cam_ip + ':81/stream'
url = api_server_url.strip() + '/detect'

cap = cv2.VideoCapture(cam_path)

def detecting():
  while True:
    _, frame = cap.read()
    frame = cv2.flip(cv2.flip(frame, 0),1)

    if not _:
        raise Exception('CAPTURE ERR')

    ret, buf = cv2.imencode('.jpg', frame)

    res = requests.post(url, files={'frame': buf})
    
    if pars_result(res.content):
      termux.Notification.notify("DETECT", time.strftime('%Y-%m-%d %H:%M:%S'))
    
    
    time.sleep(3)

    

def pars_result(res):
  return res == 'TRUE'

try:
  detecting()
  
except BaseException as e:
  termux.Notification.notify("ERROR", str(e))
  
  print("RETRY")
  
  detecting()
    
