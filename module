ma = [['B', 'C', 'D', 'F', '*', 'F', 'D', 'C', 'B'],
     ['*', '*', '*', '*', 'G', '*', '*', '*', '*'],
     ['*', 'E', '*', '*', '*', '*', '*', 'E', '*'],
     ['A', '*', 'A', '*', 'A', '*', 'A', '*', 'A'],
     ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
     ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
     ['a', '*', 'a', '*', 'a', '*', 'a', '*', 'a'],
     ['*', 'e', '*', '*', '*', '*', '*', 'e', '*'],
     ['*', '*', '*', '*', 'g', '*', '*', '*', '*'],
     ['b', 'c', 'd', 'f', '*', 'f', 'd', 'c', 'b']]

def my_turn():
    global ma
    print("플레이어1의 차례입니다.")
    print()
    print("어떤 말을 움직이시겠습니까?")
    a, b = map(int, input().split())
    selectA(a,b)

def selectA(a,b):
    global ma
    if ma[a][b] == '*':
        my_turn()

    elif ma[a][b] == 'a':
        a_rule(a,b)

    elif ma[a][b] == 'c':
        c_rule(a, b)

    elif ma[a][b] == 'f':
        f_rule(a,b)

    elif ma[a][b] == 'g':
        g_rule(a,b)

    '''elif ma[a][b] == 'b':
        b_rule(a,b)

    elif ma[a][b] == 'd':
        d_rule(a,b)

    elif ma[a][b] == 'e':
        e_rule(a,b)'''

def your_turn():
    print("플레이어2의 차례입니다.")
    print()
    print("어떤 말을 움직이시겠습니까?")
    a, b = map(int, input().split())
    selectB(a,b)


def selectB(a, b):
    global ma
    if ma[a][b] == '*':
        your_turn()

    elif ma[a][b] == 'A':
        A_rule(a, b)

    elif ma[a][b] == 'C':
        C_rule(a, b)

    elif ma[a][b] == 'F':
        F_rule(a, b)

    elif ma[a][b] == 'G':
        G_rule(a, b)

    '''elif ma[a][b] == 'B':
        B_rule(a, b)

    elif ma[a][b] == 'D':
        D_rule(a, b)

    elif ma[a][b] == 'E':
        E_rule(a, b)'''

def a_rule(a,b):
    global ma
    print("어디로 움직이시겠습니까?")
    c, d = map(int, input().split())
    if ((c == a - 1) and (d == b)) or ((c == a) and (d == b - 1)) or ((c == a) and (d == b + 1)) :
        if (c < 0) or (c > 9) or (d < 0) or (d > 8):
            print()
            print("다시 시도하세요.")
            print()
            a_rule(a, b)
        elif ma[c][d] == '*':
            temp = ma[c][d]
            ma[c][d] = ma[a][b]
            ma[a][b] = temp
            return
        else:
            ma[c][d] = ma[a][b]
            ma[a][b] = '*'
            return

    else:
        print("다시 시도하세요.")
        a_rule(a, b)


'''def b_rule(a, b):
    global ma
    c, d = map(int, input().split())
    if ((c == a - 9) and (d == b)) or ((c == a - 9) and (d == b)) or ((c == a - 8) and (d == b)) or ((c == a - 7) and (d == b)) or ((c == a - 6) and (d == b)) or ((c == a - 5) and (d == b)) or'''



def c_rule(a, b):
    global ma
    print("어디로 움직이시겠습니까?")
    c, d = map(int, input().split())
    if ((c == a + 2) and (d == b + 1)) or ((c == a + 2) and (d == b - 1)) or ((c == a + 1) and (d == b + 2)) or ((c == a + 1) and (d == b - 2)) or ((c == a - 1) and (d == b + 2)) or ((c == a - 2) and (d == b + 1)) or ((c == a - 1) and (d == b - 2)) or ((c == a - 2) and (d == b - 1)):
        if (c < 7) or (c > 9) or (d < 3) or (d > 5):
            print()
            print("다시 시도하세요.")
            print()
            f_rule(a, b)
        elif ma[c][d] == '*':
            temp = ma[c][d]
            ma[c][d] = ma[a][b]
            ma[a][b] = temp
            return
        else:
            ma[c][d] = ma[a][b]
            ma[a][b] = '*'
            return

    else:
        print("다시 시도하세요.")
        c_rule(a, b)


'''def d_rule(a, b):

def e_rule(a, b):'''

def f_rule(a, b):
    global ma
    print("어디로 움직이시겠습니까?")
    c, d = map(int, input().split())
    if ((c == a - 1) and (d == b)) or ((c == a + 1) and (d == b)) or ((c == a) and (d == b - 1)) or ((c == a) and (d == b + 1)) :
        if (c < 7) or (c > 9) or (d < 3) or (d > 5):
            print()
            print("다시 시도하세요.")
            print()
            f_rule(a, b)
        elif ma[c][d] == '*':
            temp = ma[c][d]
            ma[c][d] = ma[a][b]
            ma[a][b] = temp
            return
        else:
            ma[c][d] = ma[a][b]
            ma[a][b] = '*'
            return

    else:
        print("다시 시도하세요.")
        f_rule(a, b)


def g_rule(a, b):
    global ma
    print("어디로 움직이시겠습니까?")
    c, d = map(int, input().split())
    if ((c == a - 1) and (d == b)) or ((c == a + 1) and (d == b)) or ((c == a) and (d == b - 1)) or ((c == a) and (d == b + 1)):
        if (c < 7) or (c > 9) or (d < 3) or (d > 5):
            print()
            print("다시 시도하세요.")
            print()
            f_rule(a, b)
        elif ma[c][d] == '*':
            temp = ma[c][d]
            ma[c][d] = ma[a][b]
            ma[a][b] = temp
            return
        else:
            ma[c][d] = ma[a][b]
            ma[a][b] = '*'
            return
    else:
        print("다시 시도하세요.")


def A_rule(a, b):
    global ma
    print("어디로 움직이시겠습니까?")
    c, d = map(int, input().split())
    if ((c == a + 1) and (d == b)) or ((c == a) and (d == b - 1)) or ((c == a) and (d == b + 1)):
        if (c < 0) or (c > 9) or (d < 0) or (d > 8):
            print()
            A_rule(a, b)
        elif ma[c][d] == '*':
            temp = ma[c][d]
            ma[c][d] = ma[a][b]
            ma[a][b] = temp
            return
        else:
            ma[c][d] = ma[a][b]
            ma[a][b] = '*'
            return


'''
def B_rule(a, b):'''

def C_rule(a, b):
    global ma
    print("어디로 움직이시겠습니까?")
    c, d = map(int, input().split())
    if ((c == a + 2) and (d == b + 1)) or ((c == a + 2) and (d == b - 1)) or ((c == a + 1) and (d == b + 2)) or (
            (c == a + 1) and (d == b - 2)) or ((c == a - 1) and (d == b + 2)) or ((c == a - 2) and (d == b + 1)) or (
            (c == a - 1) and (d == b - 2)) or ((c == a - 2) and (d == b - 1)):
        if (c < 7) or (c > 9) or (d < 3) or (d > 5):
            print()
            print("다시 시도하세요.")
            print()
            f_rule(a, b)
        elif ma[c][d] == '*':
            temp = ma[c][d]
            ma[c][d] = ma[a][b]
            ma[a][b] = temp
            return
        else:
            ma[c][d] = ma[a][b]
            ma[a][b] = '*'
            return

    else:
        print("다시 시도하세요.")
        C_rule(a, b)

'''def D_rule(a, b):

def E_rule(a, b):'''

def F_rule(a, b):
    global ma
    print("어디로 움직이시겠습니까?")
    c, d = map(int, input().split())
    if ((c == a - 1) and (d == b)) or ((c == a + 1) and (d == b)) or ((c == a) and (d == b - 1)) or (
            (c == a) and (d == b + 1)):
        if (c > 2) or (d < 3) or (d > 5):
            print()
            print("다시 시도하세요.")
            print()
            f_rule(a, b)
        elif ma[c][d] == '*':
            temp = ma[c][d]
            ma[c][d] = ma[a][b]
            ma[a][b] = temp
            return
        else:
            ma[c][d] = ma[a][b]
            ma[a][b] = '*'
            return

    else:
        print("다시 시도하세요.")
        F_rule(a, b)



def G_rule(a, b):
    global ma
    print("어디로 움직이시겠습니까?")
    c, d = map(int, input().split())
    if ((c == a - 1) and (d == b)) or ((c == a + 1) and (d == b)) or ((c == a) and (d == b - 1)) or ((c == a) and (d == b + 1)):
        if (c > 2) or (d < 3) or (d > 5):
            print()
            print("다시 시도하세요.")
            print()
            f_rule(a, b)
        elif ma[c][d] == '*':
            temp = ma[c][d]
            ma[c][d] = ma[a][b]
            ma[a][b] = temp
            return
        else:
            ma[c][d] = ma[a][b]
            ma[a][b] = '*'
            return

    else:
        print("다시 시도하세요.")
        G_rule(a, b)
