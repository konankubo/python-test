import requests
import sys
 
token = 'K3NfQRXJDnZ86EQd0gvrZp1CNLoPld2rQVNeTqqesoF'
 
stdin = sys.stdin.readlines()   # 標準入力から受け取る
stdin = [line.rstrip() for line in stdin]   # 改行コードの処理
msg = '\r\n' + '\r\n'.join(stdin)
 
payload = {'message': msg}
url = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': 'Bearer ' + token}
 
try:
 res = requests.post(url, data=payload, headers=headers)
 print(f'LINE: {res.reason}')
except:
 print('Error')    # ネット接続エラーなど