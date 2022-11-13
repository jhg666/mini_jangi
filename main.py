print('이 장기는 미니 장기입니다. 1은 쫄, 2는 차, 3은 왕이며 상대방의 왕을 잡으면 이기는 게임입니다.')
print()
print("쫄과 차, 왕의 이동 범위는 기존 장기의 룰과 같습니다.")
print()
print("왕은 시작 위치에서 주변 한 칸 씩까지만 움직일 수 있으며, 그 영역을 벗어날 수는 없습니다.")
print()
print('게임을 시작하겠습니다.')
print()

a = [[2, 0, 3, 0, 2],
     [1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1],
     [2, 0, 3, 0, 2]]

while True:

    for x in a:
        print(x)

    print()
    print("움직일 말을 선택해주세요.")

    while True:
        row, column = map(int, input().split())
        if 0 <= row < 5 and 0 <= column < 5:
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
            if 0 <= row < 5 and 0 <= column < 5:
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
            print("다시 입력해 주세요.")

    if b == 2:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 5 and 0 <= column < 5:
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
            print("다시 입력해 주세요.")

    if b == 3:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 5 and 0 <= column < 5:
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
            print("다시 입력해 주세요.")

    if a[0][1] != 3 and a[0][2] != 3 and a[0][3] != 3 and a[1][1] != 3 and a[1][2] != 3 and a[1][3] != 3:
        print("게임이 끝났습니다.")
        print()
        print("승자는 플레이어 2입니다.")
        print()
        print("수고하셨습니다.")
        break

    if a[3][1] != 3 and a[3][2] != 3 and a[3][3] != 3 and a[4][1] != 3 and a[4][2] != 3 and a[4][3] != 3:
        print("게임이 끝났습니다.")
        print()
        print("승자는 플레이어 1입니다.")
        print()
        print("수고하셨습니다.")
        break
