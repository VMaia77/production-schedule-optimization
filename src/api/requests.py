import os
import requests
import json
import src.environment


url = os.getenv("URL")


def get_request():
    url_get = f'{url}status'
    response_get = requests.get(url_get)
    response_json = response_get.json()
    # print(response_json)
    return response_json


def post_request(problem_data):
    url_solver = f'{url}solve'
    response = requests.post(url_solver, json=problem_data)
    response_json = json.loads(response.content)
    # print(response_json)
    return response_json
