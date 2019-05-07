#coding:UTF-8
import requests

def main():
    url = "https://notify-api.line.me/api/notify"
    token = "zMqg4G8zLOqvusA20qn2fIHBYF723RaRfoSsIqUPWqI"
    headers = {"Authorization" : "Bearer "+ token}

    message =  'ここにメッセージを入れます'
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()