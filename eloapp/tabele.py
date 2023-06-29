from request_app import request


def kierowcyStatTestLiga(user, password, host, port, database, id):
    req = request(user, password, host, port, database)
    cursor = req.cursor()
    lista_kierowcow = []
    for i in range(500):
        query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s" % (id, i)
        cursor.execute(query)
        liczba = cursor.fetchone()[0]
        if liczba == 0:
            continue
        query_kierowcy = "select nick from kierowcy where id_kierowcy = %s" % i
        cursor.execute(query_kierowcy)
        nick = cursor.fetchone()[0]
        zmienne = [nick, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        zmienne[11] = liczba
        for x in range(1, 11):
            query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s and pozycja = %s" % (id, i, x)
            cursor.execute(query)
            pozycje = cursor.fetchone()[0]
            zmienne[x] = pozycje
        query2 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s and fl = 1" % (id, i)
        cursor.execute(query2)
        liczba_fl = cursor.fetchone()[0]
        zmienne[12] = liczba_fl
        query3 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s and fl = 1 and pozycja < 11" % (id, i)
        cursor.execute(query3)
        liczba_fl_10 = cursor.fetchone()[0]
        zmienne[13] = liczba_fl_10
        query4 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s and pp = 1" % (id, i)
        cursor.execute(query4)
        liczba_pp = cursor.fetchone()[0]
        zmienne[14] = liczba_pp
        zmienne[15] = zmienne[1] * 25 + zmienne[2] * 18 + zmienne[3] * 15 + zmienne[4] * 12 + zmienne[5] * 10 + zmienne[6] * 8 + zmienne[7] * 6 + zmienne[8] * 4 + zmienne[9] * 2 + zmienne[10] + zmienne[13]
        lista_kierowcow.append(zmienne)
    list_return = sorted(lista_kierowcow, key=lambda y: y[15], reverse=True)
    return list_return


def kierowcyStatTestLigaSplit(user, password, host, port, database, split):
    req = request(user, password, host, port, database)
    cursor = req.cursor()
    lista_kierowcow = []
    for i in range(500):
        query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s" % (split, i)
        cursor.execute(query)
        liczba = cursor.fetchone()[0]
        if liczba == 0:
            continue
        query_kierowcy = "select nick from kierowcy where id_kierowcy = %s" % i
        cursor.execute(query_kierowcy)
        nick = cursor.fetchone()[0]
        zmienne = [nick, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        zmienne[11] = liczba
        for x in range(1, 11):
            query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and pozycja = %s" % (split, i, x)
            cursor.execute(query)
            pozycje = cursor.fetchone()[0]
            zmienne[x] = pozycje
        query2 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and fl = 1" % (split, i)
        cursor.execute(query2)
        liczba_fl = cursor.fetchone()[0]
        zmienne[12] = liczba_fl
        query3 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and fl = 1 and pozycja < 11" % (split, i)
        cursor.execute(query3)
        liczba_fl_10 = cursor.fetchone()[0]
        zmienne[13] = liczba_fl_10
        query4 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and pp = 1" % (split, i)
        cursor.execute(query4)
        liczba_pp = cursor.fetchone()[0]
        zmienne[14] = liczba_pp
        zmienne[15] = zmienne[1] * 25 + zmienne[2] * 18 + zmienne[3] * 15 + zmienne[4] * 12 + zmienne[5] * 10 + zmienne[6] * 8 + zmienne[7] * 6 + zmienne[8] * 4 + zmienne[9] * 2 + zmienne[10] + zmienne[13]
        lista_kierowcow.append(zmienne)
    list_return = sorted(lista_kierowcow, key=lambda y: y[15], reverse=True)
    return list_return


def kierowcyStatTestLigaSplitGra(user, password, host, port, database, split, gra):
    req = request(user, password, host, port, database)
    cursor = req.cursor()
    lista_kierowcow = []
    for i in range(500):
        query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and gra = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s" % (split, gra, i)
        cursor.execute(query)
        liczba = cursor.fetchone()[0]
        if liczba == 0:
            continue
        query_kierowcy = "select nick from kierowcy where id_kierowcy = %s" % i
        cursor.execute(query_kierowcy)
        nick = cursor.fetchone()[0]
        zmienne = [nick, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        zmienne[11] = liczba
        for x in range(1, 11):
            query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and gra = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and pozycja = %s" % (split, gra, i, x)
            cursor.execute(query)
            pozycje = cursor.fetchone()[0]
            zmienne[x] = pozycje
        query2 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and gra = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and fl = 1" % (split, gra, i)
        cursor.execute(query2)
        liczba_fl = cursor.fetchone()[0]
        zmienne[12] = liczba_fl
        query3 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and gra = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and fl = 1 and pozycja < 11" % (split, gra, i)
        cursor.execute(query3)
        liczba_fl_10 = cursor.fetchone()[0]
        zmienne[13] = liczba_fl_10
        query4 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and gra = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and pp = 1" % (split, gra, i)
        cursor.execute(query4)
        liczba_pp = cursor.fetchone()[0]
        zmienne[14] = liczba_pp
        zmienne[15] = zmienne[1] * 25 + zmienne[2] * 18 + zmienne[3] * 15 + zmienne[4] * 12 + zmienne[5] * 10 + zmienne[6] * 8 + zmienne[7] * 6 + zmienne[8] * 4 + zmienne[9] * 2 + zmienne[10] + zmienne[13]
        lista_kierowcow.append(zmienne)
    list_return = sorted(lista_kierowcow, key=lambda y: y[15], reverse=True)
    return list_return

def kierowcyStatTestLigaSplitPomiedzy(user, password, host, port, database, split, start, stop):
    req = request(user, password, host, port, database)
    cursor = req.cursor()
    lista_kierowcow = []
    for i in range(500):
        query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and id_wyscigu between %s and %s and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s" % (split, start, stop, i)
        cursor.execute(query)
        liczba = cursor.fetchone()[0]
        if liczba == 0:
            continue
        query_kierowcy = "select nick from kierowcy where id_kierowcy = %s" % i
        cursor.execute(query_kierowcy)
        nick = cursor.fetchone()[0]
        zmienne = [nick, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        zmienne[11] = liczba
        for x in range(1, 11):
            query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and id_wyscigu between %s and %s and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and pozycja = %s" % (split, start, stop, i, x)
            cursor.execute(query)
            pozycje = cursor.fetchone()[0]
            zmienne[x] = pozycje
        query2 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and id_wyscigu between %s and %s and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and fl = 1" % (split, start, stop, i)
        cursor.execute(query2)
        liczba_fl = cursor.fetchone()[0]
        zmienne[12] = liczba_fl
        query3 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and id_wyscigu between %s and %s and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and fl = 1 and pozycja < 11" % (split, start, stop, i)
        cursor.execute(query3)
        liczba_fl_10 = cursor.fetchone()[0]
        zmienne[13] = liczba_fl_10
        query4 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and id_wyscigu between %s and %s and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and pp = 1" % (split, start, stop, i)
        cursor.execute(query4)
        liczba_pp = cursor.fetchone()[0]
        zmienne[14] = liczba_pp
        zmienne[15] = zmienne[1] * 25 + zmienne[2] * 18 + zmienne[3] * 15 + zmienne[4] * 12 + zmienne[5] * 10 + zmienne[6] * 8 + zmienne[7] * 6 + zmienne[8] * 4 + zmienne[9] * 2 + zmienne[10] + zmienne[13]
        lista_kierowcow.append(zmienne)
    list_return = sorted(lista_kierowcow, key=lambda y: y[15], reverse=True)
    return list_return

def kierowcyStatTestLigaSplitId(user, password, host, port, database, split, i):
    req = request(user, password, host, port, database)
    cursor = req.cursor()
    try:
        i = int(i)
    except ValueError:
        query_nick = "select id_kierowcy from kierowcy where nick = '%s'" % i
        cursor.execute(query_nick)
        i = cursor.fetchone()[0]
    query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s" % (split, i)
    cursor.execute(query)
    liczba = cursor.fetchone()[0]
    query_kierowcy = "select nick from kierowcy where id_kierowcy = %s" % i
    cursor.execute(query_kierowcy)
    nick = cursor.fetchone()[0]
    lista_kierowcow = [nick, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lista_kierowcow[11] = liczba
    for x in range(1, 11):
        query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and pozycja = %s" % (split, i, x)
        cursor.execute(query)
        pozycje = cursor.fetchone()[0]
        lista_kierowcow[x] = pozycje
    query2 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and fl = 1" % (split, i)
    cursor.execute(query2)
    liczba_fl = cursor.fetchone()[0]
    lista_kierowcow[12] = liczba_fl
    query3 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and fl = 1 and pozycja < 11" % (split, i)
    cursor.execute(query3)
    liczba_fl_10 = cursor.fetchone()[0]
    lista_kierowcow[13] = liczba_fl_10
    query4 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where split = '%s' and typ_ligi = 'F1' and platforma = 'PC' and id_kierowcy = %s and pp = 1" % (split, i)
    cursor.execute(query4)
    liczba_pp = cursor.fetchone()[0]
    lista_kierowcow[14] = liczba_pp
    lista_kierowcow[15] = lista_kierowcow[1] * 25 + lista_kierowcow[2] * 18 + lista_kierowcow[3] * 15 + lista_kierowcow[4] * 12 + lista_kierowcow[5] * 10 + lista_kierowcow[6] * 8 + lista_kierowcow[7] * 6 + lista_kierowcow[8] * 4 + lista_kierowcow[9] * 2 + lista_kierowcow[10] + lista_kierowcow[13]
    return lista_kierowcow

def kierowcyStatTestTor(user, password, host, port, database, id, kraj):
    req = request(user, password, host, port, database)
    cursor = req.cursor()
    lista_kierowcow = []
    for i in range(500):
        query = "select * from wyscigi_razem w left join wyscigi wy on w.id_wyscigu = wy.id where id_kierowcy = 1 and kraj = 'BH'"




        query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id left join wyscigi wy on w.id_wyscigu = wy.id_wyscigu where id_wyscigu = %s and kraj = '%s'" % (i, kraj)
        cursor.execute(query)
        liczba = cursor.fetchone()[0]
        query = "select typ_ligi from wyscigi_razem w left join ligi l on w.id_ligi = l.id left join wyscigi wy on w.id_wyscigu = wy.id_wyscigu where id_wyscigu = %s and kraj = '%s'" % (i, kraj)
        cursor.execute(query)
        typ = cursor.fetchone()[0]
        if liczba == 0 or typ not in ["F1", "F2"]:
            continue
        try:
            id = int(id)
        except ValueError:
            query_nick = "select id_kierowcy from kierowcy where nick = '%s'" % id
            cursor.execute(query_nick)
            id = cursor.fetchone()[0]
        query = "select typ_ligi from wyscigi_razem w left join ligi l on w.id_ligi = l.id left join wyscigi wy on w.id_wyscigu = wy.id_wyscigu where l.id = %s and id_wyscigu = %s and kraj = '%s'" % (id, i, kraj)


        for x in range(1, 11):
            query = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s and pozycja = %s" % (id, i, x)
            cursor.execute(query)
            pozycje = cursor.fetchone()[0]
        query2 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s and fl = 1" % (id, i)
        cursor.execute(query2)
        liczba_fl = cursor.fetchone()[0]
        query3 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s and fl = 1 and pozycja < 11" % (id, i)
        cursor.execute(query3)
        liczba_fl_10 = cursor.fetchone()[0]
        query4 = "select count(*) from wyscigi_razem w left join ligi l on w.id_ligi = l.id where l.id = %s and id_kierowcy = %s and pp = 1" % (id, i)
        cursor.execute(query4)
        liczba_pp = cursor.fetchone()[0]
    list_return = sorted(lista_kierowcow, key=lambda y: y[15], reverse=True)
    return list_return
