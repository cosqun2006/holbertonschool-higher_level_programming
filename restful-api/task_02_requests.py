#!/usr/bin/python3

import csv
import requests


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    r=requests.get(url)
    print("Status code: ", {r.status_code})

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get("title"))
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    r=requests.get(url)
    print("Status code: ", {r.status_code})
    if r.status_code == 200:
        posts = r.json()
        for post in posts:



