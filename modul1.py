class D_AW:
    def __init__(self):
        raise NotImplementedError
    def __repr__(self):
        return '<%s: %r>' % (type(self).__name__, self.dane)

class D_Program(D_AW):
    def __init__(self, program=None, dane_p=None):
        if program == None:
            self.dane = []
        else:
            self.dane = program.dane + [dane_p]
        #if program == None:
        #    self.dane = []
        #else:
        #    self.dane = (program, dane_p)
    def pokaz(self):
        print('; POCZATEK PROGRAMU')
        for dane_p in self.dane:
            dane_p.pokaz()
        print('; KONIEC PROGRAMU')

class D_Dane_F(D_AW):
    def __init__(self, a, b, c, d, e, f, g):
        self.dane = (a, b, c, d, e, f, g)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', self.dane[2] if self.dane[2] != None else '', self.dane[3] if self.dane[3] != None else '', self.dane[4] if self.dane[4] != None else '', self.dane[5] if self.dane[5] != None else '', self.dane[6] if self.dane[6] != None else '', end='')

class D_Dane_I(D_AW):
    def __init__(self, a, b):
        self.dane = (a, b)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', end='')

class D_Lista_Zmiennych_P(D_AW):
    def __init__(self, a=None):
        self.dane = a
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', end='')

class D_Lista_Zmiennych(D_AW):
    def __init__(self, a, b, c):
        self.dane = (a, b, c)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', self.dane[2] if self.dane[2] != None else '', end='')


class D_Struktura_P(D_AW):
    def __init__(self, a=None):
        self.dane = a
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', end='')

class D_Struktura(D_AW):
    def __init__(self, a, b, c):
        self.dane = (a, b, c)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', self.dane[2] if self.dane[2] != None else '', end='')


class D_Instrukcja(D_AW):
    def __init__(self, a, b=None):
        if b == None:
            self.dane = (a)
        else:
            self.dane = (a,b)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', end='')

class D_Instrukcja_If(D_AW):
    def __init__(self, a, b, c, d, e, f, g):
        self.dane = (a, b, c, d, e, f, g)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', self.dane[2] if self.dane[2] != None else '', self.dane[3] if self.dane[3] != None else '', self.dane[4] if self.dane[4] != None else '', self.dane[5] if self.dane[5] != None else '', self.dane[6] if self.dane[6] != None else '', end='')


class D_Instrukcja_While(D_AW):
    def __init__(self, a, b, c, d, e):
        self.dane = (a, b, c, d, e)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', self.dane[2] if self.dane[2] != None else '', self.dane[3] if self.dane[3] != None else '', self.dane[4] if self.dane[4] != None else '', end='')

class D_Wyrazenie_A(D_AW):
    def __init__(self, a, b=None, c=None):
        if b == None:
            self.dane = (a,)
        elif c == None:
            self.dane = (a,b)
        else:
            if a == '(':
                self.dane = (b,)
            else:
                self.dane = (b, a, c)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', self.dane[2] if self.dane[2] != None else '', end='')

class D_Lista_Wyrazenie_A(D_AW):
    def __init__(self, a=None):
        self.dane = a
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', end='')

class D_Wyrazenie_L(D_AW):
    def __init__(self, a, b, c):
        self.dane = (a, b, c)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', self.dane[2] if self.dane[2] != None else '', end='')

class D_Funkcja(D_AW):
    def __init__(self, a, b, c, d):
        self.dane = (a, b, c, d)
    def pokaz(self):
        print(self.dane[0] if self.dane[0] != None else '', self.dane[1] if self.dane[1] != None else '', self.dane[2] if self.dane[2] != None else '', self.dane[3] if self.dane[3] != None else '', end='')


def test():

    d1 = D_Dane_I('import', 'sciezka.txt')

    l1 = D_Lista_Zmiennych_P()
    i1 = D_Instrukcja('return', '22')
    s1 = D_Struktura_P(i1)
    d2 = D_Dane_F('func', 'nazwa_programu', '(', l1, ')',  i1, 'endf')

    l2_2 = D_Lista_Zmiennych_P('zmienna2')
    l2 = D_Lista_Zmiennych('zmienna1', ',', l2_2)

    wa1 = D_Wyrazenie_A('12')
    wa1_2 = D_Wyrazenie_A('10')
    wl1 = D_Wyrazenie_L(wa1, '<', wa1_2)

    i2_2 = D_Instrukcja('return', '12')
    s2_2 = D_Struktura_P(i2_2)
    i2_3 = D_Instrukcja('return', '10')
    s2_3 = D_Struktura_P(i2_3)

    i2 = D_Instrukcja_If('if', wl1, 'then', s2_2, 'else', s2_3,'endi')
    s2 = D_Struktura_P(i2)
    d3 = D_Dane_F('func', 'nazwa_programu_dwa', '(', l2, ')', s2, 'endf')

    t0 = D_Program()
    t1 = D_Program(t0, d1)
    t2 = D_Program(t0, d2)
    t3 = D_Program(t0, d3)


    t0.pokaz()
    t1.pokaz()
    t2.pokaz()
    t3.pokaz()


test()