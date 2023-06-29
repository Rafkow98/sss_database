import mariadb
from request_app import request
from prettytable import PrettyTable
import tabele


def listaLig(user, password, host, port, database):
    connection = request(user, password, host, port, database)
    print('LISTA LIG')
    cursor = connection.cursor()
    input_bool = False
    while not input_bool:
        print('L - lista lig')
        print('I - liga o danym ID')
        print('W - wyniki danej ligi')
        print('Q - wyjście')
        prog = input('Wybierz program: ')
        if prog in ['L', 'l']:
            cursor.execute("select * from ligi order by id")
            row = cursor.fetchone()
            x = PrettyTable()
            x.title = 'Lista lig'
            x.field_names = ['ID ligi', 'Nazwa ligi', 'Typ ligi', 'Platforma', 'Split', 'Gra', 'Liczba wyścigów']
            while row:
                x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])])
                row = cursor.fetchone()
            print(x)
        elif prog in ['I', 'i']:
            bool = False
            while not bool:
                bool_x = False
                while not bool_x:
                    bool_id = False
                    while not bool_id:
                        id_input = input('Podaj ID ligi: ')
                        try:
                            id = int(id_input)
                            bool_id = True
                        except ValueError:
                            print('Wybierz właściwe ID')
                    query = "select * from ligi where id = %s" % id
                    try:
                        cursor.execute(query)
                        row = cursor.fetchone()
                        if row is not None:
                            bool_x = True
                        else:
                            print("Wybierz właściwe ID")
                    except mariadb.OperationalError:
                        print('Wybierz właściwe ID')
                x = PrettyTable()
                x.title = row[1]
                x.field_names = ['Typ ligi', 'Platforma', 'Split', 'Gra', 'Liczba wyścigów']
                while row:
                    x.add_row([str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6])])
                    row = cursor.fetchone()
                print(x)
                bool = True
        elif prog in ['W', 'w']:
            input_bool_l = False
            while not input_bool_l:
                print('L - wyniki ligi o danym ID')
                print('H - wyniki danego splitu (cała historia, tylko PC)')
                print('G - wyniki danego splitu (jedna gra, tylko PC)')
                print('O - wyniki w podanym okresie (po ID wyścigu, tylko PC)')
                print('Q - wyjście')
                prog_l = input('Wybierz program: ')
                if prog_l in ['L', 'l']:
                    bool = False
                    while not bool:
                        bool_x = False
                        while not bool_x:
                            id_input = input('Podaj ID ligi: ')
                            try:
                                id_ligi = int(id_input)
                                query_l = "select nazwa_ligi from ligi where id = %s" % id_ligi
                                cursor.execute(query_l)
                                try:
                                    nazwa_ligi = cursor.fetchone()[0]
                                except TypeError:
                                    print("Liga o takim ID nie istnieje")
                                    continue
                                query_l = "select typ_ligi from ligi where id = %s" % id_ligi
                                cursor.execute(query_l)
                                f1 = cursor.fetchone()[0]
                                if f1 == "F1":
                                    bool_x = True
                                else:
                                    print(f"Liga o podanym ID została przeprowadzona w {f1}, wyniki są dostępne tylko dla lig w F1")
                            except ValueError:
                                print('Wybierz właściwe ID')
                        tab = tabele.kierowcyStatTestLiga(user, password, host, port, database, id_ligi)
                        x = PrettyTable()
                        x.title = f"Wyniki ligi o ID {id_ligi} - {nazwa_ligi}"
                        x.field_names = ['Nick', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'Liczba wyścigów', 'Liczba najszybszych okrążeń', 'Liczba najszybszych okrążeń na punktowanych pozycjach', 'Liczba pole position', 'Punkty']
                        for row in tab:
                            x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), str(row[15])])
                        print(x)
                        bool = True
                elif prog_l in ['H', 'h']:
                    bool = False
                    while not bool:
                        bool_x = False
                        while not bool_x:
                            split_input = input('Podaj split (A/B/C): ')
                            if split_input in ['A', 'a']:
                                tab = tabele.kierowcyStatTestLigaSplit(user, password, host, port, database, split='A')
                                bool_x = True
                            elif split_input in ['B', 'b']:
                                tab = tabele.kierowcyStatTestLigaSplit(user, password, host, port, database, split='B')
                                bool_x = True
                            elif split_input in ['C', 'c']:
                                tab = tabele.kierowcyStatTestLigaSplit(user, password, host, port, database, split='C')
                                bool_x = True
                            else:
                                print('Podaj prawidłowy split')
                        x = PrettyTable()
                        x.title = f"Tabela wszech czasów splitu {split_input}"
                        x.field_names = ['Nick', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'Liczba wyścigów', 'Liczba najszybszych okrążeń', 'Liczba najszybszych okrążeń na punktowanych pozycjach', 'Liczba pole position', 'Punkty']
                        for row in tab:
                            x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), str(row[15])])
                        print(x)
                        bool = True
                elif prog_l in ['G', 'g']:
                    bool = False
                    while not bool:
                        bool_x = False
                        while not bool_x:
                            split_input = input('Podaj split (A/B/C): ')
                            if split_input in ['A', 'a']:
                                split = 'A'
                                bool_x = True
                            elif split_input in ['B', 'b']:
                                split = 'B'
                                bool_x = True
                            elif split_input in ['C', 'c']:
                                split = 'C'
                                bool_x = True
                            else:
                                print('Podaj prawidłowy split')
                        bool_y = False
                        while not bool_y:
                            gra_input = input('Podaj grę (2019/2020/2021): ')
                            if gra_input in ['2019', 'F1 2019', 'f1 2019', 'F12019', 'f12019', 'F119', 'f119', '19']:
                                gra = 'F1 2019'
                                bool_y = True
                            elif gra_input in ['2020', 'F1 2020', 'f1 2020', 'F12020', 'f12020', 'F120', 'f120', '20']:
                                gra = 'F1 2020'
                                bool_y = True
                            elif gra_input in ['2021', 'F1 2021', 'f1 2021', 'F12021', 'f12021', 'F121', 'f121', '21']:
                                gra = 'F1 2021'
                                bool_y = True
                            else:
                                print('Podaj prawidłową grę')
                        tab = tabele.kierowcyStatTestLigaSplitGra(user, password, host, port, database, split=split, gra=gra)
                        x = PrettyTable()
                        x.title = f"Łączna tabela splitu {split} w grze {gra}"
                        x.field_names = ['Nick', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'Liczba wyścigów', 'Liczba najszybszych okrążeń', 'Liczba najszybszych okrążeń na punktowanych pozycjach', 'Liczba pole position', 'Punkty']
                        for row in tab:
                            x.add_row(
                                [str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), str(row[15])])
                        print(x)
                        bool = True
                elif prog_l in ['O', 'o']:
                    bool = False
                    while not bool:
                        bool_x = False
                        while not bool_x:
                            split_input = input('Podaj split (A/B/C): ')
                            if split_input in ['A', 'a']:
                                split = 'A'
                                bool_x = True
                            elif split_input in ['B', 'b']:
                                split = 'B'
                                bool_x = True
                            elif split_input in ['C', 'c']:
                                split = 'C'
                                bool_x = True
                            else:
                                print('Podaj prawidłowy split')
                        bool_y = False
                        while not bool_y:
                            bool_id = False
                            while not bool_id:
                                id_input = input('Podaj początkowe ID wyścigu: ')
                                try:
                                    id_poczatkowe = int(id_input)
                                    bool_id = True
                                except ValueError:
                                    print('Wybierz właściwe ID')
                            bool_id = False
                            while not bool_id:
                                id_input = input('Podaj końcowe ID wyścigu: ')
                                try:
                                    id_koncowe = int(id_input)
                                    bool_id = True
                                except ValueError:
                                    print('Wybierz właściwe ID')
                            bool_y = True
                        tab = tabele.kierowcyStatTestLigaSplitPomiedzy(user, password, host, port, database, split=split, start=id_poczatkowe, stop=id_koncowe)
                        x = PrettyTable()
                        x.title = f"Łączna tabela dla splitu {split} od wyścigu o ID {id_poczatkowe} do wyścigu o ID {id_koncowe}"
                        x.field_names = ['Nick', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'Liczba wyścigów', 'Liczba najszybszych okrążeń', 'Liczba najszybszych okrążeń na punktowanych pozycjach', 'Liczba pole position', 'Punkty']
                        for row in tab:
                            x.add_row([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), str(row[14]), str(row[15])])
                        print(x)
                        bool = True
                elif prog_l in ['Q', 'q']:
                    input_bool_l = True
                else:
                    print('Podaj właściwą literę')
        elif prog in ['Q', 'q']:
            input_bool = True
        else:
            print('Podaj właściwą literę')
