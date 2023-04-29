"""_summary_
The urllib package contains five moduls:
1. request
2. response
3. error
4. parse
5. robotparser
"""

from urllib import request


resp = request.urlopen("https://www.wikipedia.org")

print(type(resp))
print(dir(resp))
print(resp.code)
print(resp.peek()) # To see a portion of the data
data = resp.read() # Note: once you read the response, python closes the connection and the { resp } becomes an empty string.
html = data.decode("UTF-8") # we have to decode it, because the data is actuallt in bytes;
print(html)



# Query 2
# https://www.youtube.com/watch?v=Euc-yVzHhMI&t=5m56s

from urllib import parse

query = parse.urlencode({'v':'Euc-yVzHhMI', 't':'5m56s'})

print(query)