import json

import requests


def process(url):
    category = ("physic", "math", "chess")
    data = requests.get(url)
    if data.status_code == 200:
        response = requests.get(url).json()
        a = []
        try:
            for i in response:
                if any([i["category"] in tuple(category)]):
                    a.append(i["category"])
                else:
                    return "I can't recognize it"
        except:
            for k, v in response.items():
                if k == "category":
                    return (v)
                else:
                    return "I can't recognize it"

        list_set = set(a)
        if len(list_set) == 1:
            return (a[0])
        else:
            return "I can't recognize it"

    else:
        return "Bad Query"

# -----------------------------------------------------------
# def process(url):
#     response = requests.get(url)
#
#     if (response.status_code != 200):
#         return 'Bad Query'
#
#     books = response.json()
#
#     categories = list()
#     for book in books:
#         category = book['category']
#         if category not in categories:
#             categories.append(category)
#
#     if len(categories) == 1:
#         return categories[0]
#
#     return "I can't recognize it"


# ----------------------------------------------------------
# def process(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         if len(data) == 0:
#             return 'I can\'t recognize it'
#         if all(data[0]['category'] == i['category'] for i in data):
#             return data[0]['category']
#         else:
#             return 'I can\'t recognize it'
#     else:
#         return 'Bad Query'



# print(process("https://mocki.io/v1/627ba115-0fdf-484e-8c98-fdc5a75d2a83"))
# print(process("https://mocki.io/v1/71bd9a56-c86d-48e2-b5e4-a1df21c4bf74"))
# print(process("https://mocki.io/v1/8d4695f2-2027-4e17-8f98-88e3fc347e49"))
# print(process("https://mocki.io/v1/c0ddd9b7-370c-4502-b2b6-bb3e1ebbe520"))
# print(process("https://api.instantwebtools.net/v1/airlines"))
