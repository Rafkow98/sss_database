import mariadb
from request_app import request
from prettytable import PrettyTable


def zgloszenia(user, password, host, port, database):
    connection = request(user, password, host, port, database)
    print('ZGŁOSZENIA')
    cursor = connection.cursor()
    input_bool = False
    while not input_bool:
        print('I - zgłoszenie incydentu')
        print('R - rozpatrzenie incydentu (admin)')
        print('L - lista zgłoszeń')
        print('Q - wyjście')
        prog = input('Wybierz program: ')
        if prog in ['I', 'i']:
            cursor.execute("create table if not exists zgloszenia(id int primary key auto_increment, data datetime, nick_zglaszajacego varchar(50) character set utf8, nick_zglaszanego varchar(50) character set utf8, gp varchar(50) character set utf8, split varchar(10) character set utf8, numer_okrazenia int, dowod varchar(100) character set utf8, opis varchar(1000) character set utf8, punkty_karne int, sekundy_karne int, inne varchar(20) character set utf8, uzasadnienie varchar(1000) character set utf8)")
            nick = input('Podaj nick zgłaszającego: ')
            nick_zglaszanego = input('Podaj nick zgłaszanego: ')
            gp = input('Podaj miejsce GP: ')
            split = input('Podaj split: ')
            bool = False
            while not bool:
                okr = input('Podaj okrążenie: ')
                try:
                    okrazenie = int(okr)
                    bool = True
                except ValueError:
                    print('Wybierz właściwy numer')
            opis = input('Podaj opis incydentu: ')
            dowod = input('Podaj dowód (wideo): ')
            cursor.execute("insert into zgloszenia (data, nick_zglaszajacego, nick_zglaszanego, gp, split, numer_okrazenia, dowod, opis) values((select now()), ?, ?, ?, ?, ?, ?, ?)", (nick, nick_zglaszanego, gp, split, okrazenie, dowod, opis))
            print('Zgłoszenie wysłane pomyślnie')
            connection.commit()
        if prog in ['R', 'r']:
            bool = False
            while not bool:
                haslo = input('Podaj hasło: ')
                if haslo == password:
                    print('Panel admina')
                    bool_id = False
                    while not bool_id:
                        id_input = input('Podaj numer zgłoszenia do rozpatrzenia: ')
                        try:
                            id = int(id_input)
                            query = "select * from zgloszenia where id = %s" % id
                            try:
                                cursor.execute(query)
                                row = cursor.fetchone()
                                if row is not None:
                                    bool_id = True
                                else:
                                    print('Nie ma zgłoszenia o takim ID')
                            except mariadb.OperationalError:
                                print('Nie ma zgłoszenia o takim ID')
                        except ValueError:
                            print('Wybierz właściwe ID')
                    query2 = "select * from zgloszenia where id = %s" % id
                    cursor.execute(query2)
                    row = cursor.fetchone()
                    x = PrettyTable()
                    x.title = 'Zgłoszenie ' + id_input
                    x.field_names = ['ID', 'Data zgłoszenia', 'Nick zgłaszającego', 'Nick zgłaszanego', 'Nazwa GP', 'Split', 'Numer okrążenia', 'Dowód', 'Opis', 'Punkty karne', 'Sekundy karne', 'Inne uwagi', 'Uzasadnienie']
                    while row:
                        x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12])])
                        row = cursor.fetchone()
                    print(x)
                    bool_y = False
                    while not bool_y:
                        y = input('Czy chcesz dodać/zmienić werdykt (T - tak, N - nie)? ')
                        if y in ['T', 't']:
                            bool_y = True
                        elif y in ['N', 'n']:
                            bool = True
                        else:
                            print('Podaj właściwą literę')
                    punkty_karne = input('Podaj liczbę punktów karnych: ')
                    bool_pkt = False
                    while not bool_pkt:
                        try:
                            pk = int(punkty_karne)
                            bool_pkt = True
                        except ValueError:
                            print('Nie wpisano liczby')
                    sekundy = input('Podaj liczbę dodatkowych sekund: ')
                    bool_sec = False
                    while not bool_sec:
                        try:
                            sec = int(sekundy)
                            bool_sec = True
                        except ValueError:
                            print('Nie wpisano liczby')
                    di = input('Podaj dodatkowe informacje: ')
                    uz = input('Podaj uzasadnienie: ')
                    query_update = "update zgloszenia set punkty_karne = %s, sekundy_karne = %s, inne = '%s', uzasadnienie = '%s' where id = %s" % (pk, sec, di, uz, id)
                    cursor.execute(query_update)
                    cursor.execute("select * from zgloszenia")
                    row = cursor.fetchone()
                    x = PrettyTable()
                    x.title = 'Zaktualizowane zgłoszenie ' + id_input
                    x.field_names = ['ID', 'Data zgłoszenia', 'Nick zgłaszającego', 'Nick zgłaszanego', 'Nazwa GP', 'Split', 'Numer okrążenia', 'Dowód', 'Opis', 'Punkty karne', 'Sekundy karne', 'Inne uwagi', 'Uzasadnienie']
                    while row:
                        x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12])])
                        row = cursor.fetchone()
                    print(x)
                    connection.commit()
                else:
                    bool_x = False
                    while not bool_x:
                        x = input('Nieprawidłowe hasło, czy chcesz spróbować ponownie (T - tak, N - nie)? ')
                        if x in ['T', 't']:
                            bool_x = True
                        elif x in ['N', 'n']:
                            bool_x = True
                            bool = True
                        else:
                            print('Podaj właściwą literę')
        if prog in ['L', 'l']:
            cursor.execute("select * from zgloszenia order by id")
            row = cursor.fetchone()
            x = PrettyTable()
            x.title = 'Lista zgłoszeń'
            x.field_names = ['ID', 'Data zgłoszenia', 'Nick zgłaszającego', 'Nick zgłaszanego', 'Nazwa GP', 'Split', 'Numer okrążenia', 'Dowód', 'Opis', 'Punkty karne', 'Sekundy karne', 'Inne uwagi', 'Uzasadnienie']
            while row:
                x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12])])
                row = cursor.fetchone()
            print(x)
        elif prog in ['Q', 'q']:
            input_bool = True
        else:
            print('Podaj właściwą literę')
