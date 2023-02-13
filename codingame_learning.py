import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    s = ''
    for j in range(n):
        if j == i or j == n - i - 1:
            s += 'x'
        else:
            s += '#'
    print(s)


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

open_bracket = input()
close_bracket = input()
message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

combos = {}

for x, y in zip(open_bracket, close_bracket):
    combos[x] = y

s = []

for x in message:
    if x in combos.keys():
        s.append(x)
    elif x in combos.values():
        if x != s.pop():
            print(False)
            break
        elif x == s.pop():
            continue