import tabele
from request_app import request
from prettytable import PrettyTable


def listaKierowcow(user, password, host, port, database):
    connection = request(user, password, host, port, database)
    print('LISTA KIEROWCÓW')
    cursor = connection.cursor()
    input_bool = False
    while not input_bool:
        print('K - lista kierowców')
        print('I - kierowca o danym ID lub nicku')
        print('E - lista kierowców według rankingu ELO')
        print('W - wyniki kierowcy na danym torze')
        print('P - pojedynki kierowców')
        print('Q - wyjście')
        prog = input('Wybierz program: ')
        if prog in ['K', 'k']:
            cursor.execute("select * from kierowcy")
            row = cursor.fetchone()
            x = PrettyTable()
            x.title = 'Lista kierowców'
            x.field_names = ['ID kierowcy', 'Nick kierowcy', 'ID Discord']
            while row:
                x.add_row([str(row[0]), str(row[1]), str(row[2])])
                row = cursor.fetchone()
            print(x)
        elif prog in ['I', 'i']:
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
                        query = "select * from kierowcy where nick = '%s'" % x
                        cursor.execute(query)
                        title = x
                        try:
                            cursor.fetchone()[0]
                            bool_x = True
                        except TypeError:
                            print("Wybierz właściwy nick")
                    if x_int:
                        query = "select * from kierowcy where id_kierowcy = %s" % x_int_val
                        query2 = "select nick from kierowcy where id_kierowcy = %s" % x_int_val
                        cursor.execute(query2)
                        try:
                            title = cursor.fetchone()[0]
                            bool_x = True
                        except TypeError:
                            print("Wybierz właściwe ID")
                cursor.execute(query)
                row = cursor.fetchone()
                tab_a = tabele.kierowcyStatTestLigaSplitId(user, password, host, port, database, split='A', i=x)
                tab_b = tabele.kierowcyStatTestLigaSplitId(user, password, host, port, database, split='B', i=x)
                tab_c = tabele.kierowcyStatTestLigaSplitId(user, password, host, port, database, split='C', i=x)
                x = PrettyTable()
                x.title = 'Kierowca: ' + title
                x.field_names = ['ID kierowcy', 'Nick kierowcy', 'ID Discord', 'Liczba wyścigów - liga A', 'Liczba zwycięstw - liga A', 'Liczba podiów - liga A', 'Liczba punktów - liga A', 'Liczba wyścigów - liga B', 'Liczba zwycięstw - liga B', 'Liczba podiów - liga B', 'Liczba punktów - liga B', 'Liczba wyścigów - liga C', 'Liczba zwycięstw - liga C', 'Liczba podiów - liga C', 'Liczba punktów - liga C']
                while row:
                    x.add_row([str(row[0]), str(row[1]), str(row[2]), tab_a[11], tab_a[1], tab_a[1] + tab_a[2] + tab_a[3], tab_a[15], tab_b[11], tab_b[1], tab_b[1] + tab_b[2] + tab_b[3], tab_b[15], tab_c[11], tab_c[1], tab_c[1] + tab_c[2] + tab_c[3], tab_c[15]])
                    row = cursor.fetchone()
                print(x)
                bool = True
        elif prog in ['E', 'e']:
            input_bool_e = False
            while not input_bool_e:
                print('H - lista kierowców według rankingu ELO (cała historia)')
                print('G - lista kierowców według rankingu ELO (podana gra)')
                print('Q - wyjście')
                prog_e = input('Wybierz program: ')
                if prog_e in ['H', 'h']:
                    cursor.execute("select nick, elo from kierowcy_elo ke left join kierowcy k on ke.id_kierowcy = k.id_kierowcy where elo <> 1500 order by elo desc")
                    row = cursor.fetchone()
                    x = PrettyTable()
                    x.title = 'Ranking ELO (2019-2022)'
                    x.field_names = ['Nick kierowcy', 'ELO']
                    while row:
                        x.add_row([str(row[0]), str(row[1])])
                        row = cursor.fetchone()
                    print(x)
                elif prog_e in ['G', 'g']:
                    bool_y = False
                    while not bool_y:
                        gra_input = input('Podaj grę (2019/2020/2021): ')
                        if gra_input in ['2019', 'F1 2019', 'f1 2019', 'F12019', 'f12019', 'F119', 'f119', '19']:
                            gra = 'F1 2019'
                            cursor.execute("select nick, elo_f12019 from kierowcy_elo ke left join kierowcy k on ke.id_kierowcy = k.id_kierowcy where elo_f12019 <> 1500 order by elo_f12019 desc")
                            row = cursor.fetchone()
                            bool_y = True
                        if gra_input in ['2022', 'F1 2022', 'f1 2022', 'F12022', 'f12022', 'F122', 'f122', '22']:
                            gra = 'F1 22'
                            cursor.execute("select nick, elo_f122 from kierowcy_elo ke left join kierowcy k on ke.id_kierowcy = k.id_kierowcy where elo_f122 <> 1500 order by elo_f122 desc")
                            row = cursor.fetchone()
                            bool_y = True
                        elif gra_input in ['2020', 'F1 2020', 'f1 2020', 'F12020', 'f12020', 'F120', 'f120', '20']:
                            gra = 'F1 2020'
                            cursor.execute("select nick, elo_f12020 from kierowcy_elo ke left join kierowcy k on ke.id_kierowcy = k.id_kierowcy where elo_f12020 <> 1500 order by elo_f12020 desc")
                            row = cursor.fetchone()
                            bool_y = True
                        elif gra_input in ['2021', 'F1 2021', 'f1 2021', 'F12021', 'f12021', 'F121', 'f121', '21']:
                            gra = 'F1 2021'
                            cursor.execute("select nick, elo_f12021 from kierowcy_elo ke left join kierowcy k on ke.id_kierowcy = k.id_kierowcy where elo_f12021 <> 1500 order by elo_f12021 desc")
                            row = cursor.fetchone()
                            bool_y = True
                        else:
                            print('Podaj prawidłową grę')
                    x = PrettyTable()
                    x.title = f'Ranking ELO dla gry {gra}'
                    x.field_names = ['Nick kierowcy', 'ELO']
                    while row:
                        x.add_row([str(row[0]), str(row[1])])
                        row = cursor.fetchone()
                    print(x)
                elif prog_e in ['Q', 'q']:
                    input_bool_e = True
                else:
                    print('Podaj właściwą literę')
        elif prog in ['W', 'w']:
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
                        query = "select id_kierowcy from kierowcy where nick = '%s'" % x
                        cursor.execute(query)
                        title = x
                        try:
                            x = cursor.fetchone()[0]
                            bool_x = True
                        except TypeError:
                            print("Wybierz właściwy nick")
                    if x_int:
                        query2 = "select nick from kierowcy where id_kierowcy = %s" % x_int_val
                        cursor.execute(query2)
                        try:
                            title = cursor.fetchone()[0]
                            bool_x = True
                        except TypeError:
                            print("Wybierz właściwe ID")
                query = "select pozycja, nazwa_wyscigu, data_rozpoczecia, nazwa_ligi, split, typ_ligi from wyscigi_razem w left join wyscigi wy on w.id_wyscigu = wy.id left join ligi l on wy.id_liga = l.id where id_kierowcy = %s and kraj = '%s' and typ_ligi != 'AC'" % (x, y.upper())
                cursor.execute(query)
                row = cursor.fetchone()
                x = PrettyTable()
                x.title = f'Kierowca: {title}, tor: {y.upper()}'
                x.field_names = ['Pozycja', 'Nazwa wyścigu', 'Data', 'Liga', 'Split', 'Typ ligi']
                while row:
                    x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])])
                    row = cursor.fetchone()
                print(x)
                bool = True
        elif prog in ['P', 'p']:
            bool = False
            while not bool:
                bool_x = False
                while not bool_x:
                    x = input('Podaj ID lub nick kierowcy 1: ')
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
                        query = "select id_kierowcy from kierowcy where nick = '%s'" % x
                        cursor.execute(query)
                        kierowca_1 = x
                        try:
                            x = cursor.fetchone()[0]
                            bool_x = True
                        except TypeError:
                            print("Wybierz właściwy nick")
                    if x_int:
                        query2 = "select nick from kierowcy where id_kierowcy = %s" % x_int_val
                        cursor.execute(query2)
                        try:
                            kierowca_1 = cursor.fetchone()[0]
                            bool_x = True
                        except TypeError:
                            print("Wybierz właściwe ID")
                bool_y = False
                while not bool_y:
                    y = input('Podaj ID lub nick kierowcy 2: ')
                    try:
                        y_int_val = int(y)
                        y_int = isinstance(y_int_val, int)
                    except ValueError:
                        y_int = False
                    if not y_int:
                        y_str = isinstance(y, str)
                    else:
                        y_str = False
                    if y_str:
                        query = "select id_kierowcy from kierowcy where nick = '%s'" % y
                        cursor.execute(query)
                        kierowca_2 = y
                        try:
                            y = cursor.fetchone()[0]
                            bool_y = True
                        except TypeError:
                            print("Wybierz właściwy nick")
                    if y_int:
                        query2 = "select nick from kierowcy where id_kierowcy = %s" % y_int_val
                        cursor.execute(query2)
                        try:
                            kierowca_2 = cursor.fetchone()[0]
                            bool_y = True
                        except TypeError:
                            print("Wybierz właściwe ID")
                z = input('Podaj kod kraju: ')
                query = "select * from wyscigi where kraj = '%s'" % z
                cursor.execute(query)
                try:
                    cursor.fetchone()[0]
                except TypeError:
                    print("Niewłaściwy kod, w tabeli zostaną zawarte wszystkie wyścigi")
                    z = '%'

                query = "select t1.pozycja as poz1, t2.pozycja as poz2, nazwa_wyscigu, nazwa_ligi, gra, data_rozpoczecia from (select pozycja, id_wyscigu, id_ligi from wyscigi_razem where id_kierowcy = %s) t1 inner join (select pozycja, id_wyscigu, id_ligi from wyscigi_razem where id_kierowcy = %s) t2 on t1.id_wyscigu = t2.id_wyscigu left join wyscigi w on t1.id_wyscigu = w.id left join ligi l on t1.id_ligi = l.id where kraj like '%s' and split != 'S' and typ_ligi = 'F1'" % (x, y, z)
                cursor.execute(query)
                row = cursor.fetchone()
                if z == '%':
                    z = 'wszystkie'
                x = PrettyTable()
                x.title = f'{kierowca_1} vs {kierowca_2}, tor: {z.upper()}'
                x.field_names = [kierowca_1, kierowca_2, 'Nazwa wyścigu', 'Nazwa ligi', 'Gra', 'Data rozpoczęcia']
                lz_1_2019 = lz_2_2019 = lz_1_2020 = lz_2_2020 = lz_1_2021 = lz_2_2021 = 0
                while row:
                    if row[4] == 'F1 2019':
                        if row[0] < row[1]:
                            lz_1_2019 += 1
                        else:
                            lz_2_2019 += 1
                    if row[4] == 'F1 2020':
                        if row[0] < row[1]:
                            lz_1_2020 += 1
                        else:
                            lz_2_2020 += 1
                    if row[4] == 'F1 2021':
                        if row[0] < row[1]:
                            lz_1_2021 += 1
                        else:
                            lz_2_2021 += 1

                    x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])])
                    row = cursor.fetchone()
                print(x)
                if lz_1_2019 != 0 or lz_2_2019 != 0:
                    print(f'Bilans (F1 2019): {kierowca_1} - {kierowca_2} {lz_1_2019}:{lz_2_2019}')
                if lz_1_2020 != 0 or lz_2_2020 != 0:
                    print(f'Bilans (F1 2020): {kierowca_1} - {kierowca_2} {lz_1_2020}:{lz_2_2020}')
                if lz_1_2021 != 0 or lz_2_2021 != 0:
                    print(f'Bilans (F1 2021): {kierowca_1} - {kierowca_2} {lz_1_2021}:{lz_2_2021}')
                print(f'Bilans (ogółem): {kierowca_1} - {kierowca_2} {lz_1_2019 + lz_1_2020 + lz_1_2021}:{lz_2_2019 + lz_2_2020 + lz_2_2021}')
                bool = True


        elif prog in ['Q', 'q']:
            input_bool = True
        else:
            print('Podaj właściwą literę')
