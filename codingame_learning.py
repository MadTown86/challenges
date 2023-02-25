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

n = int(input())
for i in range(n):
    p0, p1 = [int(j) for j in input().split()]
    print(int(bin(p0)[2:])+int(bin(p1)[2:]))

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(fact(n))

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

start = int(input())

arr = [1,1]
for i in range(start-2):
    arr += [arr[-1] + arr[-2]]
print(*arr[::-1])


start = int(input())
nums = []
def fib(prev_num, num, count):
    if count > 0:
        fib(num, num+prev_num, count-1)
        nums.append(num)
fib(1,1,start-1)
nums.append(1)
print(" ".join(list(map(str,nums))))

import math

n = int(input())
y = int(input())
print(math.ceil(n * 1.2 ** y * 4))

n,*z=map(int,open(0))
m=round(sum(z)/len(z))
d=5*sorted(abs(x-m)for x in z)[n//2]
print("Keeping values between",m-d,"and",m+d)