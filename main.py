"""
0은 비어있는 칸, 1은 쫄, 2는 차, 3은 왕으로 지정.
왕은 3곱하기2칸만 움직일 수 있음.
차는 대각선 제외한 가로, 세로 제한 없이 이동 가능. 아군을 건너뛸 수는 없음.
쫄은 좌/우/앞으로 1칸 이동 가능. 뒤로는 불가능.
처음은 사람 vs 사람 대결로 만들어보고
그 다음에 인공지능을 입력한다.

"""
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
            break
    print("다시 입력해 주세요.")

if a[row][column] == 1:
    
if a[row][column] == 2:

if a[row][column] == 3:
