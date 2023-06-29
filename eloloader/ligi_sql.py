from request import request, requestPlik


def ligiSql(user, password, host, port, database):
    req = request(user, password, host, port, database, query_api='league')
    (data, connection) = req
    cursor = connection.cursor()
    cursor.execute("create table if not exists ligi (id int primary key, nazwa_ligi varchar(100) character set utf8, typ_ligi varchar(5), platforma varchar(5), split varchar(1), gra varchar(15), liczba_wyscigow int)")
    for item in data:
        item2 = item.items()
        for res in item2:
            (key, value) = res
            if key == 'id':
                id_ligi = value
            if key == 'name':
                cursor.execute("insert ignore into ligi (id, nazwa_ligi) values(?, ?)", (id_ligi, value))
                query = "select nazwa_ligi from ligi where id = %s" % id_ligi
                cursor.execute(query)
                typ = cursor.fetchone()[0]
                if typ.startswith("Formuła 1") or typ.startswith("F1"):
                    query = "update ligi set typ_ligi = 'F1' where id = %s" % id_ligi
                    cursor.execute(query)
                elif typ.startswith("Formuła 2"):
                    query = "update ligi set typ_ligi = 'F2' where id = %s" % id_ligi
                    cursor.execute(query)
                elif typ.startswith("Assetto"):
                    query = "update ligi set typ_ligi = 'AC' where id = %s" % id_ligi
                    cursor.execute(query)
                else:
                    query = "update ligi set typ_ligi = 'inne' where id = %s" % id_ligi
                    cursor.execute(query)
                if "playstation" in typ.lower():
                    query = "update ligi set platforma = 'PS4' where id = %s" % id_ligi
                    cursor.execute(query)
                elif "xbox" in typ.lower():
                    query = "update ligi set platforma = 'XBOX' where id = %s" % id_ligi
                    cursor.execute(query)
                else:
                    query = "update ligi set platforma = 'PC' where id = %s" % id_ligi
                    cursor.execute(query)
                if " c " in typ.lower() or typ[-1].lower() == 'c':
                    query = "update ligi set split = 'C' where id = %s" % id_ligi
                    cursor.execute(query)
                elif " b " in typ.lower() or typ[-1].lower() == 'b':
                    query = "update ligi set split = 'B' where id = %s" % id_ligi
                    cursor.execute(query)
                elif "#" in typ or 'Funrace' in typ or 'Gran' in typ or 'SSS555' in typ:
                    query = "update ligi set split = 'S' where id = %s" % id_ligi
                    cursor.execute(query)
                else:
                    query = "update ligi set split = 'A' where id = %s" % id_ligi
                    cursor.execute(query)
                if ("Wiosna 2020" in typ and "Formuła" in typ) or "2019" in typ:
                    query = "update ligi set gra = 'F1 2019' where id = %s" % id_ligi
                    cursor.execute(query)
                elif "Liga 2021" in typ:
                    query = "update ligi set gra = 'F1 2021' where id = %s" % id_ligi
                    cursor.execute(query)
                elif "F1 22" in typ:
                    query = "update ligi set gra = 'F1 22' where id = %s" % id_ligi
                    cursor.execute(query)
                elif "Assetto" in typ:
                    query = "update ligi set gra = 'Assetto Corsa' where id = %s" % id_ligi
                    cursor.execute(query)
                elif 'Funrace' in typ or 'Gran' in typ:
                    query = "update ligi set gra = 'inne' where id = %s" % id_ligi
                    cursor.execute(query)
                else:
                    query = "update ligi set gra = 'F1 2020' where id = %s" % id_ligi
                    cursor.execute(query)

                connection.commit()
