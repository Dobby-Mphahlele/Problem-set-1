import requests

url = 'http://127.0.0.1:5000/calculate'
data = """
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

"""

response = requests.post(url, data=data)
print(response.json())
