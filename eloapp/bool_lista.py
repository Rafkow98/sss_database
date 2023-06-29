def boolLista(input_bool):
    bool_lista = False
    while not bool_lista:
        input_menu = input('Czy chcesz powrócić do ekranu głównego aplikacji (T - tak, N - nie, wyjście z aplikacji)? ')
        if input_menu in ['T', 't']:
            bool_lista = True
            input_bool = False
        elif input_menu in ['N', 'n']:
            bool_lista = True
            input_bool = True
        else:
            print('Podaj właściwą literę')
    return input_bool
