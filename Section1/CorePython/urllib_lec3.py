'''
Topic: HOW TO Fetch Internet Resources Using The urllib Package
Author: Michael Foord
'''

import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python'}
headers = {'User-Agent': user_agent}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
request = urllib.request.Request(url, data, headers=headers)
with urllib.request.urlopen(request) as response:
    the_page = response.read()
    actual_data = the_page.decode("UTF-8")
    with open('urllib.html', 'w') as html_file:
        #html_file.write(actual_data) ==> Uncomment this before you run the code.
        pass


""" Hndling Errors 
URL ERROR
Often, URLError is raised because there is no network connection (no route to the specified server), or the specified server doesn't exist. In this case, the exception raised will have a 'reason' attribute, which is a tuple containing an error code and a text error message.

HTTP ERROR
Every HTTP response from the server contains a numeric “status code”. Sometimes the status code indicates that the server is unable to fulfil the request. The default handlers will handle some of these responses for you (for example, if the response is a “redirection” that requests the client fetch the document from a different URL, urllib will handle that for you). For those it can't handle, urlopen will raise an HTTPError. Typical errors include '404' (page not found), '403' (request forbidden), and '401' (authentication required).
"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib import parse
url = 'https://www.google.com/search'
param = {'q': 'Electric Vehicles'}
param_s = parse.urlencode(param)
search_param = param_s.encode('utf-8')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
request = Request(url, search_param, headers=headers)
try: 
    search_request = urlopen(request)
    data = search_request.read()
    data = data.decode('UTF-8')
    print(data)
except HTTPError as http_error:
    print('HTTPError', http_error)
except URLError as url_error:
    print('URLError', url_error)
else:
    print('Everything is fine')
finally:
    print('Action completed')

# Note The except HTTPError must come first, otherwise except URLError will also catch an HTTPError.
