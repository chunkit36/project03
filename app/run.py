import requests
import numpy
import time
import datetime
import os
import json
from lxml import etree

from components.io import requests_from_url
from components.io import write_file
from components.io import convert_XML2JSON

#https://www.hongkongairport.com/flightinfo-rest/rest/flights?span=1&date=2021-12-24&lang=en&cargo=false&arrival=false
global URLString
URLString = {
    "RL_S": "https://www.fehd.gov.hk/english/licensing/license/text/LP_Restaurants_EN.XML",

}

DATETOQUERY = ["2021-12-25", "2021-12-26", "2021-12-27"]
# DATETOQUERY = ["2021-12-25", "2021-12-30"]

URLLIST = []

def date_to_URL(date):
    finalURL = URLString["prefix"] + str(date) + URLString["cargo"] + "true" + URLString["arrival"] + "true"
    return finalURL

def get_data_from_HKIA_API(date):
    # for date in DATETOQUERY:
    #     URLLIST.append(requests_from_url(date))

    URL = [requests_from_url(date_to_URL(date)) for date in DATETOQUERY]

    return URL

def download_files():
    # res = requests_from_url(URLString["RL_S"], "xml")
    convert_XML2JSON(res)


def main():
    # download_files()
    # URL = get_data_from_HKIA_API(DATETOQUERY)
    # print(URL)
    # write_file("../data/", "XMAS2021.json", URL)

    root = etree.parse(r"../data/RL_S.xml")
    # with open("../data/RL_S.xml"):
        # x = open("../data/RL_S.xml")
        
    # print(etree.tostring(root))
    data = convert_XML2JSON(etree.tostring(root))
    print(data)



if __name__ == '__main__':
    main() 