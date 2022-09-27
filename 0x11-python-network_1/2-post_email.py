#!/usr/bin/python3
"""header response"""
import sys
from urllib import request, parse


if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        form_data = bytes(parse.urlencode([("email", email)]), "utf-8")
        with request.urlopen(url, data=form_data) as response:
            print(response.read().decode("utf-8"))
