from urllib import request
from urllib import parse

# x = request.urlopen('https://www.google.com')
# print(x.read())

url = "http://pythonprogramming.net"
values = {"s": "basic", "submit": "Search"}

"""
data = parse.urlencode(values)
data = data.encode('utf-8')
req = request.Request(url, data)
resp = request.urlopen(req)
respData = resp.read()
print(respData[:50])
"""

# try:
#     x = request.urlopen('https://www.google.com/search?q=test')
#     print(x.read())
# except Exception as e:
#     print(str(e))


try:
    url = "https://www.google.com/search?q=test"

    headers = {}
    # when you access a website using python, the your user-Agent in you request header is going to show that this is python and it can definitely be a bot, and websites usually block bots from getting into their website. so, to bypass this, we can change our user-Agent infomation.
    headers[
        "User-Agent"
    ] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"  # To by pass google 403 forbidden error.
    req = request.Request(url, headers=headers)

    response = request.urlopen(req)
    respdata = response.read()

    with open("urllib_lec2.text", "w") as file:
        file.write(str(respdata))

except Exception as e:
    print(str(e))
