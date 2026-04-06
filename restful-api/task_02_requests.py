#!/usr/bin/env python3
"""This module fetches and processes data from an API."""

import requests
import csv


URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print status code and titles."""
    response = requests.get(URL)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch posts and save them to a CSV file."""
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
