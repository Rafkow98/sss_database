from request import request


def kierowcySql(user, password, host, port, database, query_api):
    req = request(user, password, host, port, database, query_api)
    (data, connection) = req
    cursor = connection.cursor()
    cursor.execute("create table if not exists kierowcy (id_kierowcy int primary key, nick varchar(50) character set utf8, "
                   "id_discord bigint)")
    cursor.execute("create table if not exists kierowcy_elo (id_kierowcy int primary key, elo int, elo_f12019 int, elo_f12020 int, elo_f12021 int, elo_f122 int)")
    for item in data:
        for res in item.items():
            (key, value) = res
            if key == 'id':
                id_kierowcy = value
            if key == 'name':
                nick = value
            if key == 'discordUserId':
                cursor.execute("insert ignore into kierowcy values(?, ?, ?)", (id_kierowcy, nick, value))
                query = "insert ignore into kierowcy_elo values(%s, 1500, 1500, 1500, 1500, 1500)" % id_kierowcy
                cursor.execute(query)
                connection.commit()
