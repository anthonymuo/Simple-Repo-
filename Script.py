### sample Script ####
import os
import sys

# import Math
import requests

# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Chimezie"))
r = requests.get("https://viscom-engineering.com")
print(r.status_code)
print(r.ok)

# name = input("YourName ? ")
# print("Hello,", name)
