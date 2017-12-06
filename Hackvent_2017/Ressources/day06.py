import qreader
import requests
import sys
from io import BytesIO

countries = {}
while True:
    url = 'http://challenges.hackvent.hacking-lab.com:4200/'
    content = requests.get(url).content

    data = qreader.read(BytesIO(content))
    print(data)  # prints "Version 2"
    if "HV17" in data:
        print('Found the flag: ' + data)
        sys.exit()