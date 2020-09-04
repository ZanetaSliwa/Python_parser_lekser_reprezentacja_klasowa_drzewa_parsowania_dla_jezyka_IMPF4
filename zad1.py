import ply.lex
import math
import modul1

slowa_kluczowe = {}

tokens = (
    'LICZBA_C', 'LICZBA_RZ', 'PLUS', 'MINUS', 'RAZY', 'DZIELENIE', 'NAW_L', 'NAW_P', 'NEGACJA'
, 'ROWNE', 'ROZNE', 'MNIEJSZE', 'MNIEJSZE_ROWNE', 'PRZECINEK', 'IDENT', 'PODSTAW'
, 'SREDNIK', 'IMPORT', 'FUNC', 'ENDF', 'ENDI', 'PASS', 'IF', 'SCIEZKA'
, 'THEN', 'ELSE', 'WHILE', 'DO', 'ENDW', 'READ', 'WRITE', 'RETURN'
) + tuple(slowa_kluczowe.values())

def t_LICZBA_RZ(t):
    '[0-9]+((\.[0-9]+)|([eE]([-+]?)[0-9]+))'
    t.value = float(t.value)
    return t

def t_LICZBA_C(t):
    '[0-9]+'
    t.value = float(t.value)
    return t

def t_FUNC(t):
    'func'
    return t

def t_ENDF(t):
    'endf'
    return t

def t_ENDI(t):
    'endi'
    return t

def t_ENDW(t):
    'endw'
    return t

def t_IMPORT(t):
    'import'
    return t

def t_PASS(t):
    'pass'
    return t

def t_IF(t):
    'if'
    return t

def t_THEN(t):
    'then'
    return t

def t_ELSE(t):
    'else'
    return t

def t_WHILE(t):
    'while'
    return t

def t_READ(t):
    'read'
    return t

def t_WRITE(t):
    'write'
    return t

def t_RETURN(t):
    'return'
    return t

def t_DO(t):
    'do'
    return t

def t_SREDNIK(t):
    '\;'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'-'
    return t

def t_RAZY(t):
    r'\*'
    return t

def t_DZIELENIE(t):
    r'/'
    return t

def t_NAW_L(t):
    r'\('
    return t

def t_NAW_P(t):
    r'\)'
    return t

def t_NEGACJA(t):
    r'\~'
    return t

def t_ROWNE(t):
    r'=='
    return t

def t_PODSTAW(t):
    r'='
    return t

def t_ROZNE(t):
    r'\!\='
    return t

def t_MNIEJSZE_ROWNE(t):
    r'\<\='
    return t

def t_MNIEJSZE(t):
    r'\<'
    return t

def t_PRZECINEK(t):
    r'\,'
    return t

def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #if t.value in slowa_kluczowe:
    #    t.type = slowa_kluczowe[t.value]
    return t

def t_SCIEZKA(t):
    r'[\\a-zA-Z_][a-zA-Z_0-9]*[\.\\][a-zA-Z_0-9]*'
    return t

def t_error(t):
    print('NIESPODZIEWANY ZNAK %r!' % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \n\t\r'

lekser = ply.lex.lex()

def test_leksera():
    lekser.input(
    """To jest test leksera,
    3+3-2+6*8
    3+/-*32987 4 + / 10 20
    1 10 - + 20
    ala ma kota ()
    12(z)"""
    )
    while True:
        token = lekser.token()
        if not token:
            break
        print(token)
        print('%r %r %r %r' % (token.type, token.value, token.lineno, token.lexpos))


################### parser

import ply.yacc

precedence = (
    ('left', 'ROWNE', 'ROZNE', 'MNIEJSZE_ROWNE', 'MNIEJSZE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'RAZY', 'DZIELENIE'),
    ('right', 'NEGACJA')
)

tab_sym = {}

def p_program_dane(p):
    'program : program dane_p'
    p[0] = D_Program(p[1],p[2])

def p_program_pusty(p):
    'program : '
    p[0] = None
    #p[0] = D_Program()

#def p_program_dane(p):
#    'program : program dane'
#    p[0] = None

def p_dane_funkcja(p):
    'dane_p : FUNC IDENT NAW_L lista_zmiennych NAW_P struktura ENDF'
    p[0] = D_Dane_F(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_dane_import(p):
    'dane_p : IMPORT SCIEZKA'
    p[0] = D_Dane_I(p[1], p[2])

def p_lista_zmiennych_pusta(p):
    'lista_zmiennych : '
    p[0] = D_Lista_Zmiennych_P()

def p_lista_zmiennych_jednej(p):
    'lista_zmiennych : IDENT'
    p[0] = D_Lista_Zmiennych_P(tab_sym[p[1]])

def p_lista_zmiennych_wielu(p):
    'lista_zmiennych : IDENT PRZECINEK lista_zmiennych'
    p[0] = D_Lista_Zmiennych(p[1], p[2], p[3])

def p_struktura_pusta(p):
    'struktura : '
    p[0] = D_Struktura_P()

def p_struktura(p):
    'struktura : instrukcja'
    p[0] = D_Struktura_P(p[1])

def p_struktura_lista(p):
    'struktura : instrukcja SREDNIK struktura'
    p[0] = D_Struktura(p[1], p[2], p[3])

def p_instrukcja_pass(p):
    'instrukcja : PASS'
    p[0] = D_Instrukcja(p[1])

def p_instrukcja_if(p):
    'instrukcja : IF wyrazenie_l THEN struktura ELSE struktura ENDI'
    p[0] = D_Instrukcja_If(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_instrukcja_while(p):
    'instrukcja : WHILE wyrazenie_l DO struktura ENDW'
    p[0] = D_Istrukcja_While(p[1], p[2], p[3], p[4], p[5])

def p_instrukcja_read(p):
    'instrukcja : READ IDENT'
    p[0] = D_Instrukcja(p[2])

def p_instrukcja_write(p):
    'instrukcja : WRITE wyrazenie_a'
    p[0] = D_Instrukcja(p[2])

def p_instrukcja_podstawienie(p):
    'instrukcja : IDENT PODSTAW wyrazenie_a'
    tab_sym[p[1]] = p[3]
    p[0] = D_Wyrazenie_A(p[1], p[2], p[3])

def p_instrukcja_return(p):
    'instrukcja : RETURN wyrazenie_a'
    p[0] = D_Instrukcja(p[1], p[2])

def p_instrukcja_wywolania_funkcji(p):
    'instrukcja : funkcja'
    p[0] = D_Istrukcja(p[1])

def p_funkcja(p):
    'funkcja : IDENT NAW_L lista_wyrazen_a NAW_P'
    p[0] = D_Funkcja(p[1], p[2], p[3], p[4])

def p_wyrazenie_l_rowne(p):
    'wyrazenie_l : wyrazenie_a ROWNE wyrazenie_a'
    if(p[1] == p[3]):
        p[0] = 1
    else:
        p[0] = 0
    p[0] = D_Wyrazenie_L(p[1], p[2], p[3])

def p_wyrazenie_l_rozne(p):
    'wyrazenie_l : wyrazenie_a ROZNE wyrazenie_a'
    p[0] = int(p[1] != p[3])
    p[0] = D_Wyrazenie_L(p[1], p[2], p[3])

def p_wyrazenie_l_mniejsze_rowne(p):
    'wyrazenie_l : wyrazenie_a MNIEJSZE_ROWNE wyrazenie_a'
    p[0] = int(p[1] <= p[3])
    p[0] = D_Wyrazenie_L(p[1], p[2], p[3])

def p_wyrazenie_l_mniejsze(p):
    'wyrazenie_l : wyrazenie_a MNIEJSZE wyrazenie_a'
    p[0] = int(p[1] < p[3])
    p[0] = D_Wyrazenie_L(p[1], p[2], p[3])


def p_lista_wyrazen_a_pusta(p):
    'lista_wyrazen_a : '
    p[0] = D_Lista_Wyrazenie_A()

def p_lista_wyrazen_a_jednej(p):
    'lista_wyrazen_a : wyrazenie_a'
    p[0] = D_Lista_Wyrazenie_A(p[1])

def p_lista_wyrazen_a_wielu(p):
    'lista_wyrazen_a : wyrazenie_a PRZECINEK lista_wyrazen_a'
    p[0] = D_Wyrazenie_A(p[1], p[2], p[3])

def p_wyrazenie_a_nazwa(p):
    'wyrazenie_a : IDENT'
    p[0] = tab_sym[p[1]]
    p[0] = D_Wyrazenie_A(p[1])

def p_wyrazenie_a_liczba_rz(p):
    'wyrazenie_a : LICZBA_RZ'
    p[0] = D_Wyrazenie_A(p[1])

def p_wyrazenie_a_liczba_c(p):
    'wyrazenie_a : LICZBA_C'
    p[0] = D_Wyrazenie_A(p[1])

def p_wyrazenie_a_negacja(p):
    'wyrazenie_a : NEGACJA wyrazenie_a'
    p[0] = - p[2]
    p[0] = D_Wyrazenie_A(p[1], p[2])

def p_wyrazenie_a_nawiasy(p):
    'wyrazenie_a : NAW_L wyrazenie_a NAW_P'
    p[0] = p[2]
    p[0] = D_Wyrazenie_A(p[1], p[2])

def p_wyrazenie_a_funkcja(p):
    'wyrazenie_a : funkcja'
    p[0] = D_Wyrazenie_A(p[1])

def p_wyrazenie_a_dodawanie(p):
    'wyrazenie_a : wyrazenie_a PLUS wyrazenie_a'
    p[0] = p[1] + p[3]
    p[0] = D_Wyrazenie_A(p[1], p[2], p[3])

def p_wyrazenie_a_odejmowanie(p):
    'wyrazenie_a : wyrazenie_a MINUS wyrazenie_a'
    p[0] = p[1] - p[3]
    p[0] = D_Wyrazenie_A(p[1], p[2], p[3])

def p_wyrazenie_a_mnozenie(p):
    'wyrazenie_a : wyrazenie_a RAZY wyrazenie_a'
    p[0] = p[1] * p[3]
    p[0] = D_Wyrazenie_A(p[1], p[2], p[3])

def p_wyrazenie_a_dzielenie(p):
    'wyrazenie_a : wyrazenie_a DZIELENIE wyrazenie_a'
    p[0] = p[1] / p[3]
    p[0] = D_Wyrazenie_A(p[1], p[2], p[3])

def p_error(p):
    print("Błąd składniowy: '%s'." % p)

parser = ply.yacc.yacc()

def test():

    
    print('Interaktywny test:')
    a ='ok'
    while len(a) > 0:
        a = input()
        print(parser.parse(a))


test_leksera()
#test()