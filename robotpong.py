#!/usr/bin/env python

import sys
import os
import time
from collections import defaultdict

directions = {
    'S': (0, 1),
    'L': (-1, 1),
    'R': (1, 1),
}


def draw(columns, rows, field):
    for y in range(rows):
        for x in range(columns):
            s = '['
            if 'ball' in field[x, y]:
                s += 'b'
            if 'r1' in field[x, y]:
                s += '1'
            if 'r2' in field[x, y]:
                s += '2'
            if 'obs' in field[x, y]:
                s += 'o'

            for i in range(4 - len(s)):
                s += '-'

            s += ']'

            sys.stdout.write(s)

        sys.stdout.write('\n')


def finish(r1, r2, ball_pos, sequence):
    print('Robot1 At [{},{}]'.format(r1[1], r1[0]))
    print('Robot2 At [{},{}]'.format(r2[1], r2[0]))
    print('Ball At [{},{}]'.format(ball_pos[1], ball_pos[0]))
    print('Sequence: ' + str(''.join(sequence)))


# Get the stuff
rows, columns = map(int, raw_input().split(','))
field = defaultdict(list)
sequence = []

r1 = (int(raw_input()), 0)
r2 = (int(raw_input()), rows - 1)

field[r1] = ['r1']
field[r2] = ['r2']

if raw_input() == '1':
    ball_pos = r1[:]
    field[ball_pos].append('ball')
else:
    ball_pos = r2[:]
    field[ball_pos].append('ball')

ball_vel = (0, 0)

num_obstacles = int(raw_input())
obstacle_positions = []

for i in range(num_obstacles):
    y, x = map(int, raw_input().split(','))
    if y != 0 and y != (rows - 1):
        field[x, y].append('obs')
        obstacle_positions.append((x, y))

moves = list(raw_input())
moves.reverse()

# play
while True:
    # if the ball is at a robot, get thrown
    if ball_pos == r1:
        try:
            m = moves.pop()
        except:
            # No more moves
            print("This game does not have a Winner.")
            break
        # print('Robot 1 throwing in dir ' + m)
        sequence.append(m)

        if m == 'L' and r1[0] == 0:
            dx, dy = directions['R']
        elif m == 'R' and r1[0] == columns - 1:
            dx, dy = directions['L']
        else:
            dx, dy = directions[m]

        ball_vel = dx, dy

    if ball_pos == r2:
        try:
            m = moves.pop()
        except:
            print("This game does not have a Winner.")
            break
        # print('Robot 2 throwing in dir ' + m)
        sequence.append(m)

        if m == 'L' and r2[0] == 0:
            dx, dy = directions['R']
        elif m == 'R' and r2[0] == columns - 1:
            dx, dy = directions['L']
        else:
            dx, dy = directions[m]

        ball_vel = dx, dy * -1

    x, y = ball_pos
    dx, dy = ball_vel

    # move according to ball vel
    nx, ny = x + dx, y + dy

    # hit an obstacle
    if (nx, ny) in obstacle_positions:
        if not dx:
            # if no dx, then we are going straight up/down
            dy = dy * -1
        else:
            # otherwise change horizontal direction
            dx = dx * -1

    # hit the right wall
    if nx == columns - 1:
        dx = dx * -1

    # hit the left wall
    if nx == 0:
        dx = dx * -1

    ball_pos = nx, ny
    ball_vel = dx, dy

    field[x, y].remove('ball')
    field[ball_pos].append('ball')

    # move r1
    if ball_pos[0] >= r1[0]:
        dx = 1
    else:
        dx = -1

    if r1[0] == columns - 1 and dx == 1:
        dx = -1

    x, y = r1
    r1 = x + dx, y

    field[x, y].remove('r1')
    field[r1].append('r1')

    # move r2
    if ball_pos[0] >= r2[0]:
        dx = 1
    else:
        dx = -1

    if r2[0] == columns - 1 and dx == 1:
        dx = -1

    x, y = r2
    r2 = x + dx, y

    field[x, y].remove('r2')
    field[r2].append('r2')

    # end turn
    # os.system('clear')
    # draw(columns, rows, field)
    # print('  ')
    # time.sleep(0.1)

    # game end
    if ball_pos[1] == 0 and r1 != ball_pos:
        # in top row and no robot catching
        print('Winner: Robot2')
        break
    if ball_pos[1] == rows - 1 and r2 != ball_pos:
        # in bottom row and no robot catching
        print('Winner: Robot1')
        break

finish(r1, r2, ball_pos, sequence)
