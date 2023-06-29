import mariadb
import sys


def request(user, password, host, port, database):
    try:
        connection = mariadb.connect(user=user, password=password, host=host, port=port, database=database)
    except mariadb.Error as ex:
        print(f"An error occurred while connecting to MariaDB: {ex}")
        sys.exit(1)

    return connection
