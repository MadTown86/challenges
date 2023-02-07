import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
m1 = False
m2 = False
m3 = False
m4 = False
count = 0
# game loop
while count <= 100:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    xmov = light_x - initial_tx
    ymov = light_y - initial_ty

    lx = light_x
    ly = light_y
    x = initial_tx
    y = initial_ty
    rise = ly - y
    run = lx - x if lx - x != 0 else 1
    slope = rise // run
    line_equation = slope*x
    count += 1
    break
    # if light_x != initial_tx and light_y != initial_ty and abs(xmov) == abs(ymov):
    #     if xmov > 0 and ymov > 0:
    #         print('SE')
    #     elif xmov > 0 and ymov < 0:
    #         print('NE')
    #     elif xmov < 0 and ymov > 0:
    #         print('SW')
    #     else:
    #         print('NW')
    # elif light_x != initial_tx and light_y != initial_ty:
    #     if abs(xmov) > abs(ymov):
    #         if xmov > 0 and ymov > 0:
    #             print('E')
    #         elif xmov > 0 and ymov < 0:
    #             print('E')
    #         elif xmov < 0 and ymov > 0:
    #             print('W')
    #         else:
    #             print('W')
    #     else:
    #         if xmov > 0 and ymov > 0:
    #             print('S')
    #         elif xmov > 0 and ymov < 0:
    #             print('N')
    #         elif xmov < 0 and ymov > 0:
    #             print('S')
    #         else:
    #             print('N')
    # elif light_x == initial_tx and light_y != initial_ty:
    #     if ymov > 0:
    #         print('S')
    #     else:
    #         print('N')
    # elif light_x != initial_tx and light_y == initial_ty:
    #     if xmov > 0:
    #         print('E')
    #     else:
    #         print('W')


if __name__ == '__main__':
    pass