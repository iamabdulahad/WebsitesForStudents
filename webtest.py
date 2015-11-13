# !/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  + "Chrome/46.0.2490.80 Safari/537.36"
}

with open('sites.txt') as site:
    for i in site:
        print(i[:len(i)-1])
        time = 0
        for t in range(3):
            try:
                r = requests.get(i[:len(i)-1], timeout=10, headers=headers)
            except:
               time += 1
            else:
                if r.status_code == requests.codes.ok:
                    print("go")
                else:
                    print("need verify！")
        if time == 3:
            exit(1)