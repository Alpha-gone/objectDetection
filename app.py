import termux
import cv2
import requests
import sys
import time

if __name__ == '__main__':
    api_server_url = sys.argv[0]

colab_url='http://192b-34-142-140-175.ngrok-free.app'

video_path= 'http://192.168.1.76:81/stream'
url = colab_url.strip() + '/detect'
cap = cv2.VideoCapture(video_path)

while True:
    _, frame = cap.read()
    frame = cv2.flip(cv2.flip(frame, 0),1)

    if not _:
        break

    ret, buf = cv2.imencode('.jpg', frame)

    res = requests.post(url, files={'frame': buf})
    print(res.content)

    time.sleep(1)

    termux.Notification.notify("Hello", "World")