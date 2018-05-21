#!/usr/bin/python

import os
import pymarc

path = './'

def get_place_of_pub(record):
    try:
        place_of_pub = record['']['']
        print(place_of_pub)
        with open('out.txt', 'a') as f:
            print(place_of_pub, file=f)
    except Exception as e:
        print(e)

for file in os.listdir(path):
    if file.endswith('.xml'):
        pymarc.map_xml(get_place_of_pub, path + file)
