"""_summary_
    This modules runs a code that prints out a password {hub_password} which I saved as an environment variable on my system.
    This is useful in cases where you want to hide some informations in your code such as database passwords e.t.c.
"""
# import os

# hub_password = os.environ.get('HUB_PASSWORD')
# print(hub_password)

from os import getenv

x = getenv("HUB_PASSWORD")
print(x)
