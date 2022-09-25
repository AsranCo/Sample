import json

import requests


def process(url):
    data = requests.get(url)
    if data.status_code == 200:
        response = requests.get(url).json()
        try:
            for i in response:
                print(i["category"])
        except:
            for k, v in response.items():
                if k == "category":
                    print(v)
    else:
        return "Bad Query"


process("https://mocki.io/v1/627ba115-0fdf-484e-8c98-fdc5a75d2a83")
process("https://mocki.io/v1/71bd9a56-c86d-48e2-b5e4-a1df21c4bf74")
# process("https://mocki.io/v1/8d4695f2-2027-4e17-8f98-88e3fc347e49")
