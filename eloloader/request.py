from urllib.request import Request, urlopen
import json
import mariadb
import sys
from urllib.error import HTTPError


def request(user, password, host, port, database, query_api):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                            'AppleWebKit/537.11 (KHTML, like Gecko) '
                            'Chrome/23.0.1271.64 Safari/537.11',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
              'Accept-Encoding': 'none',
              'Accept-Language': 'en-US,en;q=0.8',
              'Connection': 'keep-alive'}
    url1 = 'https://www.simsprintseries.pl/api/'+query_api
    url = Request(url1, headers=header)
    json_object = urlopen(url)
    data = json.load(json_object)
    json_object.close()
    try:
        connection = mariadb.connect(user=user, password=password, host=host, port=port, database=database)
    except mariadb.Error as ex:
        print(f"An error occurred while connecting to MariaDB: {ex}")
        sys.exit(1)

    return data, connection

def requestPlik(user, password, host, port, database, plik):
    json_object = open(plik)
    data = json.load(json_object)
    json_object.close()
    try:
        connection = mariadb.connect(user=user, password=password, host=host, port=port, database=database)
    except mariadb.Error as ex:
        print(f"An error occurred while connecting to MariaDB: {ex}")
        sys.exit(1)

    return data, connection
