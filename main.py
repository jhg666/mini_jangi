print('파이썬으로 만들어진 장기입니다. 1은 쫄, 2는 차, 3은 상, 4는 마, 5는 포, 6은 사, 7은 왕이며 상대방의 왕을 잡으면 이기는 게임입니다.')
print()
print("기물의 움직임은 기존 장기의 법칙과 동일합니다.")
print()
print("기물을 선택하실 때, 그리고 움직이실 때 세로의 좌표, 가로의 좌표 순으로 입력하시면 됩니다.")
print()
print("좌표는 0에서 시작하며, 아래로 내려갈수록 세로의 좌표의 숫자는 커지고, 오른쪽으로 갈수록 가로의 좌표의 숫자는 커집니다.")
print()
print('게임을 시작하겠습니다.')
print()

a = [[2, 3, 4, 6, 0, 6, 4, 3, 2],
     [0, 0, 0, 0, 7, 0, 0, 0, 0],
     [0, 5, 0, 0, 0, 0, 0, 5, 0],
     [1, 0, 1, 0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 1, 0, 1],
     [0, 5, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 0, 0, 7, 0, 0, 0, 0],
     [2, 3, 4, 6, 0, 6, 4, 3, 2]]

while True:

    for x in a:
        print(x)

    print()
    print("움직일 말을 선택해주세요.")

    while True:
        row, column = map(int, input().split())
        if 0 <= row < 10 and 0 <= column < 9:
            if a[row][column] != 0:
                b = a[row][column]
                a[row][column] = 0
                break
        print("다시 입력해 주세요.")

    print()
    print("선택한 말을 어디로 이동 시킬 건가요?")

    if b == 1:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 10 and 0 <= column < 9:
                if a[row][column] == 0:
                    a[row][column] = 1
                    break
                if a[row][column] == 1:
                    a[row][column] = 1
                    break
                if a[row][column] == 2:
                    a[row][column] = 1
                    break
                if a[row][column] == 3:
                    a[row][column] = 1
                    break
                if a[row][column] == 4:
                    a[row][column] = 1
                    break
                if a[row][column] == 5:
                    a[row][column] = 1
                    break
                if a[row][column] == 6:
                    a[row][column] = 1
                    break
                if a[row][column] == 7:
                    a[row][column] = 1
                    break
            print("다시 입력해 주세요.")

    if b == 2:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 10 and 0 <= column < 9:
                if a[row][column] == 0:
                    a[row][column] = 2
                    break
                if a[row][column] == 1:
                    a[row][column] = 2
                    break
                if a[row][column] == 2:
                    a[row][column] = 2
                    break
                if a[row][column] == 3:
                    a[row][column] = 2
                    break
                if a[row][column] == 4:
                    a[row][column] = 2
                    break
                if a[row][column] == 5:
                    a[row][column] = 2
                    break
                if a[row][column] == 6:
                    a[row][column] = 2
                    break
                if a[row][column] == 7:
                    a[row][column] = 2
                    break
            print("다시 입력해 주세요.")

    if b == 3:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 10 and 0 <= column < 9:
                if a[row][column] == 0:
                    a[row][column] = 3
                    break
                if a[row][column] == 1:
                    a[row][column] = 3
                    break
                if a[row][column] == 2:
                    a[row][column] = 3
                    break
                if a[row][column] == 3:
                    a[row][column] = 3
                    break
                if a[row][column] == 4:
                    a[row][column] = 3
                    break
                if a[row][column] == 5:
                    a[row][column] = 3
                    break
                if a[row][column] == 6:
                    a[row][column] = 3
                    break
                if a[row][column] == 7:
                    a[row][column] = 3
                    break
            print("다시 입력해 주세요.")

    if b == 4:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 10 and 0 <= column < 9:
                if a[row][column] == 0:
                    a[row][column] = 4
                    break
                if a[row][column] == 1:
                    a[row][column] = 4
                    break
                if a[row][column] == 2:
                    a[row][column] = 4
                    break
                if a[row][column] == 3:
                    a[row][column] = 4
                    break
                if a[row][column] == 4:
                    a[row][column] = 4
                    break
                if a[row][column] == 5:
                    a[row][column] = 4
                    break
                if a[row][column] == 6:
                    a[row][column] = 4
                    break
                if a[row][column] == 7:
                    a[row][column] = 4
                    break
            print("다시 입력해 주세요.")

    if b == 5:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 10 and 0 <= column < 9:
                if a[row][column] == 0:
                    a[row][column] = 5
                    break
                if a[row][column] == 1:
                    a[row][column] = 5
                    break
                if a[row][column] == 2:
                    a[row][column] = 5
                    break
                if a[row][column] == 3:
                    a[row][column] = 5
                    break
                if a[row][column] == 4:
                    a[row][column] = 5
                    break
                if a[row][column] == 5:
                    a[row][column] = 5
                    break
                if a[row][column] == 6:
                    a[row][column] = 5
                    break
                if a[row][column] == 7:
                    a[row][column] = 5
                    break
            print("다시 입력해 주세요.")

    if b == 6:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 10 and 0 <= column < 9:
                if a[row][column] == 0:
                    a[row][column] = 6
                    break
                if a[row][column] == 1:
                    a[row][column] = 6
                    break
                if a[row][column] == 2:
                    a[row][column] = 6
                    break
                if a[row][column] == 3:
                    a[row][column] = 6
                    break
                if a[row][column] == 4:
                    a[row][column] = 6
                    break
                if a[row][column] == 5:
                    a[row][column] = 6
                    break
                if a[row][column] == 6:
                    a[row][column] = 6
                    break
                if a[row][column] == 7:
                    a[row][column] = 6
                    break
            print("다시 입력해 주세요.")

    if b == 7:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 10 and 0 <= column < 9:
                if a[row][column] == 0:
                    a[row][column] = 7
                    break
                if a[row][column] == 1:
                    a[row][column] = 7
                    break
                if a[row][column] == 2:
                    a[row][column] = 7
                    break
                if a[row][column] == 3:
                    a[row][column] = 7
                    break
                if a[row][column] == 4:
                    a[row][column] = 7
                    break
                if a[row][column] == 5:
                    a[row][column] = 7
                    break
                if a[row][column] == 6:
                    a[row][column] = 7
                    break
                if a[row][column] == 7:
                    a[row][column] = 7
                    break
            print("다시 입력해 주세요.")

    if a[0][3] != 7 and a[0][4] != 7 and a[0][5] != 7 and a[1][3] != 7 and a[1][4] != 7 and a[1][5] != 7 and a[2][3] != 7 and a[2][4] != 7 and a[2][5] != 7:
        print("게임이 끝났습니다.")
        print()
        print("승자는 플레이어 2입니다.")
        print()
        print("수고하셨습니다.")
        break

    if a[7][3] != 7 and a[7][4] != 7 and a[7][5] != 7 and a[8][3] != 7 and a[8][4] != 7 and a[8][5] != 7 and a[9][3] != 7 and a[9][4] != 7 and a[9][5] != 7:
        print("게임이 끝났습니다.")
        print()
        print("승자는 플레이어 1입니다.")
        print()
        print("수고하셨습니다.")
        break

