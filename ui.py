import module
import tkinter
turn = 0

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

root = tkinter.Tk()
root.title("장기 게임")
canvas = tkinter.Canvas(root, width=540, height=600, bg="white")
canvas.pack()

print("파이썬으로 해보는 장기 게임입니다. 좌표를 입력하여 말을 움직이세요. - 현재 기술적 문제로 차, 상, 포는 움직이지 못합니다. ")
print()
print("좌표를 입력하여 말을 움직이세요. 이때 가로 좌표는 0~9까지, 세로 좌표는 0~8까지 있으며, 가로를 먼저 입력해주시기를 바랍니다.")
print()

for row in range(10):
    for column in range(9):
        if (ma[row][column] == 'a') or (ma[row][column] == 'A'):
            canvas.create_rectangle(column * 60, row * 60, column * 60 + 60, row * 60 + 60, fill="blue")
        elif (ma[row][column] == 'b') or (ma[row][column] == 'B'):
            canvas.create_rectangle(column * 60, row * 60, column * 60 + 60, row * 60 + 60, fill="green")
        elif (ma[row][column] == 'c') or (ma[row][column] == 'C'):
            canvas.create_rectangle(column * 60, row * 60, column * 60 + 60, row * 60 + 60, fill="red")
        elif (ma[row][column] == 'd') or (ma[row][column] == 'D'):
            canvas.create_rectangle(column * 60, row * 60, column * 60 + 60, row * 60 + 60, fill="yellow")
        elif (ma[row][column] == 'e') or (ma[row][column] == 'E'):
            canvas.create_rectangle(column * 60, row * 60, column * 60 + 60, row * 60 + 60, fill="indigo")
        elif (ma[row][column] == 'f') or (ma[row][column] == 'F'):
            canvas.create_rectangle(column * 60, row * 60, column * 60 + 60, row * 60 + 60, fill="violet")
        elif (ma[row][column] == 'g') or (ma[row][column] == 'G'):
            canvas.create_rectangle(column * 60, row * 60, column * 60 + 60, row * 60 + 60, fill="pink")
        else:
            canvas.create_rectangle(column * 60, row * 60, column * 60 + 60, row * 60 + 60, fill="gray")

while True:

    for x in ma:
        print(x)

    module.my_turn()

    if (ma[0][3] != "G") and (ma[0][4] != "G") and (ma[0][5] != "G") and (ma[1][3] != "G") and (ma[1][4] != "G") and (ma[1][5] != "G") and (ma[2][3] != "G") and (ma[2][4] != "G") and (ma[2][5] != "G"):
        print("플레이어 1이 승리하셨습니다. 수고하셨습니다.")
        break

    module.your_turn()

    if (ma[7][3] != "g") and (ma[7][4] != "g") and (ma[7][5] != "g") and (ma[8][3] != "g") and (ma[8][4] != "g") and (ma[8][5] != "g") and (ma[9][3] != "g") and (ma[9][4] != "g") and (ma[9][5] != "g"):
        print("플레이어2가 승리하셨습니다. 수고하셨습니다.")
        break


    root.mainloop()
