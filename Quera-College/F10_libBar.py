import requests
import json
from requests import get


def process(book):
    if book["category"] == "math":
        list_lib = get("http://127.0.0.1:8000/math/").json()
        if any(book['name'] == i['name'] for i in list_lib):
            return "bad query"
        else:
            requests.post("http://127.0.0.1:8000/math/", data=book)

    elif book["category"] == "physic":
        list_lib = get("http://127.0.0.1:8000/physic/").json()
        if any(book['name'] == i['name'] for i in list_lib):
            return "bad query"
        else:
            requests.post("http://127.0.0.1:8000/physic/", data=book)
    elif book["category"] == "chess":
        list_lib = get("http://127.0.0.1:8000/chess/").json()
        if any(book['name'] == i['name'] for i in list_lib):
            return "bad query"
        else:
            requests.post("http://127.0.0.1:8000/chess/", data=book)


# ---------------------------------------------
# import requests
#
# def process(data):
#     url = "http://127.0.0.1:8000/"
#     url += data["category"]
#     url += "/"
#     response = requests.get(url)
#     books = response.json()
#     for book in books:
#         if book["name"] == data["name"]:
#             return "bad query"
#     requests.post(url, data)
