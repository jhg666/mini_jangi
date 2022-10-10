"""
0은 비어있는 칸, 1은 쫄, 2는 차, 3은 왕으로 지정.

왕은 3곱하기2칸만 움직일 수 있음.
차는 대각선 제외한 가로, 세로 제한 없이 이동 가능. 아군을 건너뛸 수는 없음.
쫄은 좌/우/앞으로 1칸 이동 가능. 뒤로는 불가능.
처음은 사람 vs 사람 대결로 만들어보고
그 다음에 인공지능을 입력한다.

말 하나를 옮기면 다른 말을 옮기도록 while 문을 쓴다.

말에 대한 규칙을 코드 내부에서 잡는 것은 나중으로 미룬다.

상대방의 왕을 잡으면 while을 탈출, 즉 게임 끝.

일단 턴제부터 정한다.
"""

print('이 장기는 미니 장기입니다. 1은 쫄, 2는 차, 3은 왕이며 상대방의 왕을 잡으면 이기는 게임입니다.')

print('게임을 시작하겠습니다.')

while True:

    a = [[2, 0, 3, 0, 2],
         [1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1],
         [2, 0, 3, 0, 2]]

    for x in a:
        print(x)

    while True:
        row, column = map(int, input().split())
        if 0 <= row < 5 and 0 <= column < 5:
            if a[row][column] != 0:
                b = a[row][column]
                break
        print("다시 입력해 주세요.")

    print("선택한 말을 어디로 이동시킬 건가요?")

    if b == 1:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 5 and 0 <= column < 5:
                if a[row][column] != 0:
                    c = a[row][column]
                    c == 1
                    b == 0
                    break
            print("다시 입력해 주세요.")

    if b == 2:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 5 and 0 <= column < 5:
                if a[row][column] != 0:
                    break
            print("다시 입력해 주세요.")

    if b == 3:
        while True:
            row, column = map(int, input().split())
            if 0 <= row < 5 and 0 <= column < 5:
                if a[row][column] != 0:
                    break
            print("다시 입력해 주세요.")
