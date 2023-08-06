import urllib.request
import urllib.request as req

with req.urlopen('http://python.org/') as response:
    html = response.read()

# print(html)


reqs = urllib.request.Request('http://python.org/')
# with urllib.request.urlopen(reqs) as response:
#    the_page = response.read()

print(str(reqs))
