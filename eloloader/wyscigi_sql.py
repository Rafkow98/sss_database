from urllib.error import HTTPError
from request import request, requestPlik


def wyscigiSql(user, password, host, port, database):
    req = request(user, password, host, port, database, query_api='event')
    (data, connection) = req
    cursor = connection.cursor()
    cursor.execute("create table if not exists wyscigi_temp (id int primary key, nazwa_wyscigu varchar(50) character set utf8, "
                   "kraj varchar(2), stream_link varchar(100), data_rozpoczecia datetime, id_liga int)")
    cursor.execute("create table if not exists wyscigi (id int primary key, nazwa_wyscigu varchar(50) character set utf8, "
                   "kraj varchar(2), stream_link varchar(100), data_rozpoczecia datetime, id_liga int, p1 int, p2 int, p3 int, pp int, fl int)")

    for item in data:
        for res in item.items():
            (key, value) = res
            if key == 'id':
                id_wyscigu = value
            if key == 'name':
                nazwa = value
            if key == 'stream':
                stream = value
            if key == 'starts':
                start = value
            if key == 'country':
                kraj = value
            if key == 'relatedleague':
                list = [(k, v) for k, v in value.items()]
                for i in list:
                    (key, value) = i
                    if key == 'id':
                        cursor.execute("insert ignore into wyscigi_temp values(?, ?, ?, ?, ?, ?)",
                                       (id_wyscigu, nazwa, kraj, stream, start, value))
                        connection.commit()
    for race in range(900):
        try:
            req = request(user, password, host, port, database, query_api='event/' + str(race))
            (data_api, connection) = req
            cursor = connection.cursor()
            cursor.execute(
                "create table if not exists wyscigi_razem (pozycja int, id_kierowcy int, id_wyscigu int, id_ligi int, pp int, fl int, dnf int, dsq int)")
            cursor.execute("select id_wyscigu from wyscigi_razem order by id_wyscigu desc limit 1")
            try:
                id_wyscigu = cursor.fetchone()[0]
            except TypeError:
                id_wyscigu = 0
            if race not in range(int(id_wyscigu) + 1):
                print(str(race) + 'test wyścigi')
                for item in data_api['races']:
                    for item2 in item['results']:
                        for res in item2['driver'].items():
                            (key, value) = res
                            if key == 'id':
                                query_ligi = "select l.id from wyscigi_temp w left join ligi l on w.id_liga = l.id where w.id = %s" % race
                                cursor.execute(query_ligi)
                                liga = cursor.fetchone()[0]
                                cursor.execute("insert ignore into wyscigi_razem values(?, ?, ?, ?, ?, ?, ?, ?)", (
                                item2['position'], value, race, liga, item2['pole'], item2['lap'], item2['dnf'],
                                item2['dsq']))
                                connection.commit()
        except HTTPError as err:
            if err.code == 404:
                continue
            else:
                raise
    for item in data:
        for res in item.items():
            (key, value) = res
            if key == 'id':
                id_wyscigu = value
            if key == 'name':
                nazwa = value
            if key == 'stream':
                stream = value
            if key == 'starts':
                start = value
            if key == 'country':
                kraj = value
            if key == 'relatedleague':
                list = [(k, v) for k, v in value.items()]
                for i in list:
                    (key, value) = i
                    if key == 'id':
                        query2 = "select typ_ligi from wyscigi_temp w left join ligi l on w.id_liga = l.id where w.id = %s" % id_wyscigu
                        cursor.execute(query2)
                        typ = cursor.fetchone()[0]
                        try:
                            print(str(id_wyscigu) + typ)
                        except TypeError:
                            print(str(id_wyscigu) + 'TypeError wyścigi')
                        if typ == 'F1':
                            query = "select id_kierowcy from wyscigi_temp w left join wyscigi_razem r on w.id = r.id_wyscigu where id_wyscigu = %s and r.pozycja = 1" % id_wyscigu
                            cursor.execute(query)
                            try:
                                p1 = cursor.fetchone()[0]
                            except TypeError:
                                p1 = 'null'
                            query = "select id_kierowcy from wyscigi_temp w left join wyscigi_razem r on w.id = r.id_wyscigu where id_wyscigu = %s and r.pozycja = 2" % id_wyscigu
                            cursor.execute(query)
                            try:
                                p2 = cursor.fetchone()[0]
                            except TypeError:
                                p2 = 'null'
                            query = "select id_kierowcy from wyscigi_temp w left join wyscigi_razem r on w.id = r.id_wyscigu where id_wyscigu = %s and r.pozycja = 3" % id_wyscigu
                            cursor.execute(query)
                            try:
                                p3 = cursor.fetchone()[0]
                            except TypeError:
                                p3 = 'null'
                            query = "select id_kierowcy from wyscigi_temp w left join wyscigi_razem r on w.id = r.id_wyscigu where id_wyscigu = %s and r.pp = 1" % id_wyscigu
                            cursor.execute(query)
                            try:
                                pole = cursor.fetchone()[0]
                            except TypeError:
                                pole = 'null'
                            query = "select id_kierowcy from wyscigi_temp w left join wyscigi_razem r on w.id = r.id_wyscigu where id_wyscigu = %s and r.fl = 1" % id_wyscigu
                            cursor.execute(query)
                            try:
                                fl = cursor.fetchone()[0]
                            except TypeError:
                                fl = 'null'
                            cursor.execute("insert ignore into wyscigi values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                           (id_wyscigu, nazwa, kraj, stream, start, value, p1, p2, p3, pole, fl))
                        else:
                            cursor.execute("insert ignore into wyscigi values(?, ?, ?, ?, ?, ?, null, null, null, null, null)",
                                           (id_wyscigu, nazwa, kraj, stream, start, value))
                        connection.commit()
    for x in range(100):
        query_liczba = "update ligi set liczba_wyscigow = (select count(*) from wyscigi where id_liga = %s) where id = %s" % (x, x)
        cursor.execute(query_liczba)
    cursor.execute("drop table wyscigi_temp")
    connection.commit()
