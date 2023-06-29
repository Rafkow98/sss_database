import math
import mariadb
import sys
from kierowcy_sql import kierowcySql


# Function to calculate the Probability


def Probability(rating1, rating2):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))


# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B.
def EloRating(Ra, Rb, K, d):
    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)

    # Case -1 When Player A wins
    # Updating the Elo Ratings
    if (d == 1):
        Ra = Ra + K * (1 - Pa)


    # Case -2 When Player B wins
    # Updating the Elo Ratings
    else:
        Ra = Ra + K * (0 - Pa)

    return round(Ra)

    #print("Updated Ratings:-")
    #print("Ra =", round(Ra)," Rb =", round(Rb))


# Driver code

# Ra and Rb are current ELO ratings


#Ra = int(input("Ra: "))
#Rb = int(input("Rb: "))
#K = 30
#d = int(input("Ra wins?: "))
#EloRating(Ra, Rb, K, d)


def kierowcyEloSqlTest(user, password, host, port, database):
    try:
        connection = mariadb.connect(user=user, password=password, host=host, port=port, database=database)
    except mariadb.Error as ex:
        print(f"An error occurred while connecting to MariaDB: {ex}")
        sys.exit(1)
    cursor = connection.cursor()
    cursor.execute("select w.id from wyscigi_razem wr left join wyscigi w on wr.id_wyscigu = w.id order by w.id desc limit 1")
    try:
        ost_wyscig_data = cursor.fetchone()[0]
    except TypeError:
        ost_wyscig_data = 0
    print(ost_wyscig_data)
    for race in range(int(ost_wyscig_data), 700):
        elo_rating = 0
        elo_rating_2019 = 0
        query_rok = "select substr(data_rozpoczecia, 1, 4) from wyscigi_razem w left join wyscigi wy on w.id_wyscigu = wy.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_rok)
        try:
            rok = cursor.fetchone()[0]
        except TypeError:
            print('elo TypeError' + str(race))
            continue
        query_typ = "select typ_ligi from wyscigi_razem w left join ligi l on w.id_ligi = l.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_typ)
        typ = cursor.fetchone()[0]
        query_platforma = "select platforma from wyscigi_razem w left join ligi l on w.id_ligi = l.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_platforma)
        platforma = cursor.fetchone()[0]
        query_split = "select split from wyscigi_razem w left join ligi l on w.id_ligi = l.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_split)
        split_fetch = cursor.fetchone()[0]
        query_gra = "select gra from wyscigi_razem w left join ligi l on w.id_ligi = l.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_gra)
        gra = cursor.fetchone()[0]
        query_count = "select count(*) from wyscigi_razem where id_wyscigu = %s" % race
        cursor.execute(query_count)
        count = cursor.fetchone()[0] + 1
        '''if int(rok) == 2019:
            if typ == 'F1' and platforma == 'PC' and split_fetch != 'S' and gra == "F1 2019":
                for i in range(1, count):
                    query_id_a = "select id_kierowcy from wyscigi_razem where id_wyscigu = %s and pozycja = %s" % (
                        race, i)
                    cursor.execute(query_id_a)
                    id_a = cursor.fetchone()[0]
                    query_a = "select elo from kierowcy_elo where id_kierowcy = %s" % id_a
                    cursor.execute(query_a)
                    a = cursor.fetchone()[0]
                    query_fl = "select fl from wyscigi_razem where id_wyscigu = %s and id_kierowcy = %s" % (race, id_a)
                    cursor.execute(query_fl)
                    fl_fetch = cursor.fetchone()[0]
                    if fl_fetch == 1:
                        fl = 3
                    else:
                        fl = 0
                    query_pp = "select pp from wyscigi_razem where id_wyscigu = %s and id_kierowcy = %s" % (
                        race, id_a)
                    cursor.execute(query_pp)
                    pp_fetch = cursor.fetchone()[0]
                    if pp_fetch == 1:
                        pp = 3
                    else:
                        pp = 0
                    query_dnf = "select dnf from wyscigi_razem where id_wyscigu = %s and id_kierowcy = %s" % (
                        race, id_a)
                    cursor.execute(query_dnf)
                    dnf_fetch = cursor.fetchone()[0]
                    if dnf_fetch == 1:
                        dnf = 0.5
                    else:
                        dnf = 1
                    if split_fetch.lower() == 'c':
                        split = 30
                    elif split_fetch.lower() == 'b':
                        split = 15
                    elif split_fetch.lower() == 'a':
                        split = 0
                    for j in range(1, count):
                        if j == i:
                            continue
                        else:
                            query_id_b = "select id_kierowcy from wyscigi_razem where id_wyscigu = %s and pozycja = %s" % (
                                race, j)
                            cursor.execute(query_id_b)
                            id_b = cursor.fetchone()[0]
                            query_b = "select elo from kierowcy_elo where id_kierowcy = %s" % id_b
                            cursor.execute(query_b)
                            b = cursor.fetchone()[0]
                            if i > j:
                                ra_wins = 0
                            else:
                                ra_wins = 1
                            K = 6
                            elo_def = EloRating(a, b, K, ra_wins)
                            elo_rating += elo_def - a
                            query_a_rok = "select elo_f12019 from kierowcy_elo where id_kierowcy = %s" % id_a
                            cursor.execute(query_a_rok)
                            a_rok = cursor.fetchone()[0]
                            query_b_rok = "select elo_f12019 from kierowcy_elo where id_kierowcy = %s" % id_b
                            cursor.execute(query_b_rok)
                            b_rok = cursor.fetchone()[0]
                            elo_def_rok = EloRating(a_rok, b_rok, K, ra_wins)
                            elo_rating_2019 += elo_def_rok - a_rok
                    new_elo = a + elo_rating * dnf + fl + pp - split
                    new_elo_2019 = a_rok + elo_rating_2019 * dnf + fl + pp - split
                    query_new_elo = "update kierowcy_elo set elo = %s, elo_f12019 = %s where id_kierowcy = %s" % (
                    new_elo, new_elo_2019, id_a)
                    cursor.execute(query_new_elo)
                    connection.commit()
                    elo_rating = 0
                    elo_rating_2019 = 0'''

    for race in range(int(ost_wyscig_data), 700):
        elo_rating = 0
        elo_rating_2019 = 0
        elo_rating_2020 = 0
        elo_rating_2021 = 0
        elo_rating_22 = 0
        query_rok = "select substr(data_rozpoczecia, 1, 4) from wyscigi_razem w left join wyscigi wy on w.id_wyscigu = wy.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_rok)
        try:
            rok = cursor.fetchone()[0]
        except TypeError:
            print('elo TypeError' + str(race))
            continue
        query_typ = "select typ_ligi from wyscigi_razem w left join ligi l on w.id_ligi = l.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_typ)
        typ = cursor.fetchone()[0]
        query_platforma = "select platforma from wyscigi_razem w left join ligi l on w.id_ligi = l.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_platforma)
        platforma = cursor.fetchone()[0]
        query_split = "select split from wyscigi_razem w left join ligi l on w.id_ligi = l.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_split)
        split_fetch = cursor.fetchone()[0]
        query_gra = "select gra from wyscigi_razem w left join ligi l on w.id_ligi = l.id where id_wyscigu = %s limit 1" % race
        cursor.execute(query_gra)
        gra = cursor.fetchone()[0]
        query_count = "select count(*) from wyscigi_razem where id_wyscigu = %s" % race
        cursor.execute(query_count)
        count = cursor.fetchone()[0] + 1
        if int(rok) == 2022:
            if typ == 'F1' and platforma == 'PC':
                for i in range(1, count):
                    query_id_a = "select id_kierowcy from wyscigi_razem where id_wyscigu = %s and pozycja = %s" % (
                        race, i)
                    cursor.execute(query_id_a)
                    id_a = cursor.fetchone()[0]
                    query_a = "select elo from kierowcy_elo where id_kierowcy = %s" % id_a
                    cursor.execute(query_a)
                    a = cursor.fetchone()[0]
                    query_fl = "select fl from wyscigi_razem where id_wyscigu = %s and id_kierowcy = %s" % (race, id_a)
                    cursor.execute(query_fl)
                    fl_fetch = cursor.fetchone()[0]
                    if fl_fetch == 1:
                        fl = 3
                    else:
                        fl = 0
                    query_pp = "select pp from wyscigi_razem where id_wyscigu = %s and id_kierowcy = %s" % (
                        race, id_a)
                    cursor.execute(query_pp)
                    pp_fetch = cursor.fetchone()[0]
                    if pp_fetch == 1:
                        pp = 3
                    else:
                        pp = 0
                    query_dnf = "select dnf from wyscigi_razem where id_wyscigu = %s and id_kierowcy = %s" % (
                        race, id_a)
                    cursor.execute(query_dnf)
                    dnf_fetch = cursor.fetchone()[0]
                    if dnf_fetch == 1:
                        dnf = 0.5
                    else:
                        dnf = 1
                    if split_fetch.lower() == 'c':
                        split = 30
                    elif split_fetch.lower() == 'b':
                        split = 15
                    else:
                        split = 0
                    if gra == "F1 2019":
                        for j in range(1, count):
                            if j == i:
                                continue
                            else:
                                query_id_b = "select id_kierowcy from wyscigi_razem where id_wyscigu = %s and pozycja = %s" % (
                                race, j)
                                cursor.execute(query_id_b)
                                id_b = cursor.fetchone()[0]
                                query_b = "select elo from kierowcy_elo where id_kierowcy = %s" % id_b
                                cursor.execute(query_b)
                                b = cursor.fetchone()[0]
                                if i > j:
                                    ra_wins = 0
                                else:
                                    ra_wins = 1
                                K = 6
                                elo_def = EloRating(a, b, K, ra_wins)
                                elo_rating += elo_def - a
                                query_a_rok = "select elo_f12019 from kierowcy_elo where id_kierowcy = %s" % id_a
                                cursor.execute(query_a_rok)
                                a_rok = cursor.fetchone()[0]
                                query_b_rok = "select elo_f12019 from kierowcy_elo where id_kierowcy = %s" % id_b
                                cursor.execute(query_b_rok)
                                b_rok = cursor.fetchone()[0]
                                elo_def_rok = EloRating(a_rok, b_rok, K, ra_wins)
                                elo_rating_2019 += elo_def_rok - a_rok
                        new_elo = a + elo_rating * dnf + fl + pp - split
                        new_elo_2019 = a_rok + elo_rating_2019 * dnf + fl + pp - split
                        query_new_elo = "update kierowcy_elo set elo = %s, elo_f12019 = %s where id_kierowcy = %s" % (new_elo, new_elo_2019, id_a)
                        cursor.execute(query_new_elo)
                        connection.commit()
                        elo_rating = 0
                        elo_rating_2019 = 0
                    elif gra == "F1 2020":
                        for j in range(1, count):
                            if j == i:
                                continue
                            else:
                                query_id_b = "select id_kierowcy from wyscigi_razem where id_wyscigu = %s and pozycja = %s" % (
                                    race, j)
                                cursor.execute(query_id_b)
                                id_b = cursor.fetchone()[0]
                                query_b = "select elo from kierowcy_elo where id_kierowcy = %s" % id_b
                                cursor.execute(query_b)
                                b = cursor.fetchone()[0]
                                if i > j:
                                    ra_wins = 0
                                else:
                                    ra_wins = 1
                                K = 6
                                elo_def = EloRating(a, b, K, ra_wins)
                                elo_rating += elo_def - a
                                query_a_rok = "select elo_f12020 from kierowcy_elo where id_kierowcy = %s" % id_a
                                cursor.execute(query_a_rok)
                                a_rok = cursor.fetchone()[0]
                                query_b_rok = "select elo_f12020 from kierowcy_elo where id_kierowcy = %s" % id_b
                                cursor.execute(query_b_rok)
                                b_rok = cursor.fetchone()[0]
                                elo_def_rok = EloRating(a_rok, b_rok, K, ra_wins)
                                elo_rating_2020 += elo_def_rok - a_rok
                        new_elo = a + elo_rating * dnf + fl + pp - split
                        new_elo_2020 = a_rok + elo_rating_2020 * dnf + fl + pp - split
                        query_new_elo = "update kierowcy_elo set elo = %s, elo_f12020 = %s where id_kierowcy = %s" % (
                        new_elo, new_elo_2020, id_a)
                        cursor.execute(query_new_elo)
                        connection.commit()
                        elo_rating = 0
                        elo_rating_2020 = 0
                    elif gra == "F1 2021":
                        for j in range(1, count):
                            if j == i:
                                continue
                            else:
                                query_id_b = "select id_kierowcy from wyscigi_razem where id_wyscigu = %s and pozycja = %s" % (
                                    race, j)
                                cursor.execute(query_id_b)
                                id_b = cursor.fetchone()[0]
                                query_b = "select elo from kierowcy_elo where id_kierowcy = %s" % id_b
                                cursor.execute(query_b)
                                b = cursor.fetchone()[0]
                                if i > j:
                                    ra_wins = 0
                                else:
                                    ra_wins = 1
                                K = 6
                                elo_def = EloRating(a, b, K, ra_wins)
                                elo_rating += elo_def - a
                                query_a_rok = "select elo_f12021 from kierowcy_elo where id_kierowcy = %s" % id_a
                                cursor.execute(query_a_rok)
                                a_rok = cursor.fetchone()[0]
                                query_b_rok = "select elo_f12021 from kierowcy_elo where id_kierowcy = %s" % id_b
                                cursor.execute(query_b_rok)
                                b_rok = cursor.fetchone()[0]
                                elo_def_rok = EloRating(a_rok, b_rok, K, ra_wins)
                                elo_rating_2021 += elo_def_rok - a_rok
                        new_elo = a + elo_rating * dnf + fl + pp - split
                        new_elo_2021 = a_rok + elo_rating_2021 * dnf + fl + pp - split
                        query_new_elo = "update kierowcy_elo set elo = %s, elo_f12021 = %s where id_kierowcy = %s" % (
                        new_elo, new_elo_2021, id_a)
                        cursor.execute(query_new_elo)
                        connection.commit()
                        if id_a == 133:
                            print(f'pozycja: {i}, id: {id_a}, race: {race}, old_elo: {a_rok}, elo_rating: {elo_rating_2021}, split: {split}, new_elo: {new_elo_2021}')
                        if id_a == 325:
                            print(f'pozycja: {i}, id: {id_a}, race: {race}, old_elo: {a_rok}, elo_rating: {elo_rating_2021}, split: {split}, new_elo: {new_elo_2021}')
                        elo_rating = 0
                        elo_rating_2021 = 0
                    elif gra == "F1 22":
                        for j in range(1, count):
                            if j == i:
                                continue
                            else:
                                query_id_b = "select id_kierowcy from wyscigi_razem where id_wyscigu = %s and pozycja = %s" % (
                                    race, j)
                                cursor.execute(query_id_b)
                                id_b = cursor.fetchone()[0]
                                query_b = "select elo from kierowcy_elo where id_kierowcy = %s" % id_b
                                cursor.execute(query_b)
                                b = cursor.fetchone()[0]
                                if i > j:
                                    ra_wins = 0
                                else:
                                    ra_wins = 1
                                K = 6
                                elo_def = EloRating(a, b, K, ra_wins)
                                elo_rating += elo_def - a
                                query_a_rok = "select elo_f122 from kierowcy_elo where id_kierowcy = %s" % id_a
                                cursor.execute(query_a_rok)
                                a_rok = cursor.fetchone()[0]
                                query_b_rok = "select elo_f122 from kierowcy_elo where id_kierowcy = %s" % id_b
                                cursor.execute(query_b_rok)
                                b_rok = cursor.fetchone()[0]
                                elo_def_rok = EloRating(a_rok, b_rok, K, ra_wins)
                                elo_rating_22 += elo_def_rok - a_rok
                        new_elo = a + elo_rating * dnf + fl + pp - split
                        new_elo_22 = a_rok + elo_rating_22 * dnf + fl + pp - split
                        query_new_elo = "update kierowcy_elo set elo = %s, elo_f122 = %s where id_kierowcy = %s" % (
                        new_elo, new_elo_22, id_a)
                        cursor.execute(query_new_elo)
                        connection.commit()
                        if id_a == 453:
                            print(f'boci3k: pozycja: {i}, id: {id_a}, race: {race}, old_elo: {a_rok}, elo_rating: {elo_rating_22}, split: {split}, new_elo: {new_elo_22}')
                        elo_rating = 0
                        elo_rating_22 = 0
