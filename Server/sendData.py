import requests

url = "http://127.0.0.1:8000/languages/"

try:
    headers = {
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "2cb3fa76-1400-48c3-b05a-3be004417d29,f746c8a4-bab3-427f-a370-e091546f28d9",
        'Host': "127.0.0.1:8000",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "0",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    stn = {"name": "ruby","paradigm": "no"}
    response = requests.request("POST", url, data = stn, headers=headers)

    print(response.text)
 
except Exception as e:
    print(e)