import mariadb
from request_app import request
from prettytable import PrettyTable


def wynikiWyscigow(user, password, host, port, database):
    connection = request(user, password, host, port, database)
    print('WYNIKI WYŚCIGÓW')
    cursor = connection.cursor()
    input_bool = False
    while not input_bool:
        print('L - lista wyścigów')
        print('W - wyniki wyścigu o danym ID')
        print('K - wyniki danego kierowcy w wyścigach')
        print('T - wyścigi na danym torze')
        print('Q - wyjście')
        prog = input('Wybierz program: ')
        if prog in ['L', 'l']:
            cursor.execute("select w.id, nazwa_wyscigu, stream_link, data_rozpoczecia, nazwa_ligi, k.nick, k1.nick, k2.nick, k3.nick, k4.nick from wyscigi w left join kierowcy k on w.p1 = k.id_kierowcy left join kierowcy k1 on w.p2 = k1.id_kierowcy left join kierowcy k2 on w.p3 = k2.id_kierowcy left join kierowcy k3 on w.pp = k3.id_kierowcy left join kierowcy k4 on w.fl = k4.id_kierowcy left join ligi l on w.id_liga = l.id")
            row = cursor.fetchone()
            x = PrettyTable()
            x.field_names = ['ID', 'Nazwa wyścigu', 'Stream', 'Data rozpoczęcia', 'Nazwa ligi', 'P1', 'P2', 'P3', 'Pole position', 'Najszybsze okrążenie']
            while row:
                x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9])])
                row = cursor.fetchone()
            print(x)
        elif prog in ['W', 'w']:
            bool = False
            while not bool:
                bool_x = False
                while not bool_x:
                    try:
                        id = int(input('Podaj ID wyścigu: '))
                    except TypeError:
                        print('Wybierz właściwe ID')
                    query = "select pozycja, nick, nazwa_wyscigu, nazwa_ligi, ww.pp, ww.fl, dnf, dsq from wyscigi_razem ww left join kierowcy k on ww.id_kierowcy = k.id_kierowcy left join wyscigi w on ww.id_wyscigu = w.id left join ligi l on ww.id_ligi = l.id where id_wyscigu = %s" % id
                    try:
                        cursor.execute(query)
                        bool_x = True
                    except mariadb.ProgrammingError:
                        print('Nie ma wyścigu o podanym ID')
                row = cursor.fetchone()
                x = PrettyTable()
                x.field_names = ['Pozycja', 'Nick', 'Nazwa wyścigu', 'Nazwa ligi', 'Pole position', 'Najszybsze okrążenie', 'DNF', 'DSQ']
                while row:
                    x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7])])
                    row = cursor.fetchone()
                print(x)
                bool = True
        elif prog in ['K', 'k']:
            bool = False
            while not bool:
                bool_x = False
                while not bool_x:
                    x = input('Podaj ID lub nick kierowcy: ')
                    try:
                        x_int_val = int(x)
                        x_int = isinstance(x_int_val, int)
                    except ValueError:
                        x_int = False
                    if not x_int:
                        x_str = isinstance(x, str)
                    else:
                        x_str = False
                    if x_str:
                        query = "select pozycja, nazwa_wyscigu, nazwa_ligi, data_rozpoczecia, w.pp as pole, w.fl as fl, w.dnf as dnf, w.dsq as dsq from wyscigi_razem w left join kierowcy k on w.id_kierowcy = k.id_kierowcy left join wyscigi ww on w.id_wyscigu = ww.id left join ligi l on w.id_ligi = l.id where nick = '%s' order by cast(data_rozpoczecia as datetime)" % x
                        title = x
                    if x_int:
                        query = "select pozycja, nazwa_wyscigu, nazwa_ligi, data_rozpoczecia, w.pp as pole, w.fl as fl, w.dnf as dnf, w.dsq as dsq from wyscigi_razem w left join kierowcy k on w.id_kierowcy = k.id_kierowcy left join wyscigi ww on w.id_wyscigu = ww.id left join ligi l on w.id_ligi = l.id where k.id_kierowcy = %s order by cast(data_rozpoczecia as datetime)" % x_int_val
                        query2 = "select nick from kierowcy where id_kierowcy = %s" % x_int_val
                        cursor.execute(query2)
                        title = cursor.fetchone()[0]
                    try:
                        cursor.execute(query)
                        row = cursor.fetchone()
                        if row is not None:
                            bool_x = True
                        else:
                            print("Wybierz właściwe ID lub nick")
                    except mariadb.OperationalError as err:
                        print(err.args)
                        print('Wybierz właściwe ID lub nick')
                x = PrettyTable()
                x.title = 'Kierowca: ' + title
                x.field_names = ['Pozycja', 'Nazwa wyścigu', 'Nazwa ligi', 'Data rozpoczęcia', 'Pole position', 'Najszybsze okrążenie', 'DNF', 'DSQ']
                while row:
                    x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7])])
                    row = cursor.fetchone()
                print(x)
                bool = True
        elif prog in ['T', 't']:
            bool = False
            while not bool:
                bool_y = False
                while not bool_y:
                    y = input('Podaj kod kraju: ')
                    query = "select * from wyscigi where kraj = '%s'" % y
                    cursor.execute(query)
                    try:
                        cursor.fetchone()[0]
                        bool_y = True
                    except TypeError:
                        print("Wybierz właściwy kod kraju")
                query = "select nazwa_wyscigu, data_rozpoczecia, nazwa_ligi, split, typ_ligi from wyscigi w left join ligi l on w.id_liga = l.id where kraj = '%s' and (typ_ligi = 'F1' or typ_ligi = 'F2')" % (y.upper())
                cursor.execute(query)
                row = cursor.fetchone()
                x = PrettyTable()
                x.title = f'Wyścigi na torze: {y.upper()}'
                x.field_names = ['L.p.', 'Nazwa wyścigu', 'Data', 'Liga', 'Split', 'Typ ligi']
                lp = 1
                while row:
                    x.add_row([str(lp), str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4])])
                    row = cursor.fetchone()
                    lp += 1
                print(x)
                bool = True
        elif prog in ['Q', 'q']:
            input_bool = True
        else:
            print('Podaj właściwą literę')
