from ligi_sql import ligiSql
from wyscigi_sql import wyscigiSql
from elo_sql_test import kierowcyEloSqlTest
from kierowcy_sql import kierowcySql


user = 'UŻYTKOWNIK'
password = 'HASŁO'
host = 'NAZWA_HOSTA'
port = 3306
database = 'NAZWA_BAZY'


if __name__ == '__main__':
    ligiSql(user, password, host, port, database)
    wyscigiSql(user, password, host, port, database)
    kierowcySql(user, password, host, port, database, query_api='driver')
    kierowcyEloSqlTest(user, password, host, port, database)
