import requests

try:

    print("Enter 1 to add locally\n 2 To add data to remote server")
    x = int(input())
    if x==1:
        url = "http://127.0.0.1:8000/temp/temp/"
    elif x==2:
        url = "http://167.71.234.104:8000/temp/temp/"
    
    headers = {
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "503d19f1-6d52-4b42-95f3-a36aebb6f05c,24f16764-9ee1-4315-96aa-0228f31c1e92",
        'Host': "127.0.0.1:8000",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "0",
       # 'Referer': "http://127.0.0.1:8000/temp/temp",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    stn = {"data":0001.222, "anamoly":False}
    response = requests.request("POST", url, data = stn, headers=headers)

    print(response.text)


except Exception as e:
    print(e)