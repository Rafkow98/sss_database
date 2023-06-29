from wyscigi import wynikiWyscigow
from lista_lig import listaLig
from bool_lista import boolLista
from lista_kierowcow import listaKierowcow
from zgloszenia import zgloszenia


user = 'UŻYTKOWNIK'
password = 'HASŁO'
host = 'NAZWA_HOSTA'
port = 3306
database = 'NAZWA_BAZY'


if __name__ == '__main__':
    input_bool = False
    while not input_bool:
        print('L - ligi')
        print('W - wyścigi i wyniki')
        print('K - kierowcy')
        print('Z - zgłoszenia')
        print('Q - wyjście')
        x = input('Wybierz program: ')
        if x in ['L', 'l']:
            listaLig(user, password, host, port, database)
            input_bool = boolLista(input_bool)
        elif x in ['W', 'w']:
            wynikiWyscigow(user, password, host, port, database)
            input_bool = boolLista(input_bool)
        elif x in ['K', 'k']:
            listaKierowcow(user, password, host, port, database)
            input_bool = boolLista(input_bool)
        elif x in ['Z', 'z']:
            zgloszenia(user, password, host, port, database)
            input_bool = boolLista(input_bool)
        elif x in ['Q', 'q']:
            input_bool = True
        else:
            print('Nieprawidłowy program, wybierz jeszcze raz')
