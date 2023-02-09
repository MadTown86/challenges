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

# light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
count = 0
def main(light_x, light_y, initial_tx, initial_ty):
    LX = light_x
    LY = light_y
    side_a = lambda x: abs(LX - x)**2
    side_b = lambda y: abs(LY - y)**2
    side_c = lambda x, y: math.sqrt(side_a(x) + side_b(y))
    moves = {
        'N': (0, -1),
        'S': (0, 1),
        'E': (1, 0),
        'W': (-1, 0),
        'NE': (1, -1),
        'NW': (-1, -1),
        'SE': (1, 1),
        'SW': (-1, 1)
    }
    count = 0
    # game loop
    while count <= 100:
        # remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

        if light_x == initial_tx and light_y == initial_ty:
            print(f'YOU MADE IT IN : {count} moves')
            break
        elif light_x == initial_tx and light_y != initial_ty:
            if initial_ty > light_y:
                print('N')
                initial_ty -= 1
                count += 1
                continue
            else:
                print('S')
                initial_ty += 1
                count += 1
                continue
        elif light_x != initial_tx and light_y == initial_ty:
            if initial_tx > light_x:
                print('W')
                initial_tx -= 1
                count += 1
                continue
            else:
                print('E')
                initial_tx += 1
                count += 1
                continue
        else:
            hypo_bin = []
            for key, item in moves.items():
                hypo_bin.append((side_c(initial_tx + item[0], initial_ty + item[1]), key, ))

            for res in hypo_bin:
                print(res)

            print(min(hypo_bin)[1])

            xmov, ymov = moves[min(hypo_bin)[1]]
            initial_tx += xmov
            initial_ty += ymov

            count += 1

if __name__ == "__main__":
    main(31, 4, 5, 4)
