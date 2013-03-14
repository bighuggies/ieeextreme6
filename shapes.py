#!/usr/bin/env python

import sys


def get_input():
    rows, columns = raw_input().split()
    numbers = raw_input().split()
    bitstring = ''
    bitmap = []

    for number in numbers:
        bin_string = bin(int(number))[2:]
        fill_string = '0' * (8 - len(bin_string))

        bitstring += fill_string + bin_string

    for x in range(int(rows)):
        bitmap.append([])
        for y in range(int(columns)):
            bitmap[x].append(bitstring[x * int(columns) + y])

    return bitmap


def draw(bitmap):
    for x in range(len(bitmap[0])):
        for y in range(len(bitmap)):
            if bitmap[y][x] == '1':
                sys.stdout.write('X')
            else:
                sys.stdout.write('-')

        sys.stdout.write('\n')


def find(bitmap):
    for x, column in enumerate(bitmap):
        for y, row in enumerate(column):
            if bitmap[x][y] == '1':
                return x, y


def direction(bitmap, x, y):
    print('Turning at ' + str((x, y)))

    try:
        # up
        if bitmap[x][y - 1] == '1':
            print('Going up')
            return lambda x, y: (x, y - 1)
    except:
        pass

    try:
        # right
        if bitmap[x + 1][y] == '1':
            print('Going right')
            return lambda x, y: (x + 1, y)
    except:
        pass

    try:
        # down
        if bitmap[x][y + 1] == '1':
            print('Going down')
            return lambda x, y: (x, y + 1)
    except:
        pass

    try:
        # left
        if bitmap[x - 1][y] == '1':
            print('Going left')
            return lambda x, y: (x - 1, y)
    except:
        pass

    print('Going nowhere')
    draw(bitmap)


def trace(bitmap, next, shape, x, y):
    shape['points'].append((x, y))

    nx, ny = next(x, y)

    if bitmap[nx][ny] == '1':
        erase(bitmap, ((x, y),))
        shape = trace(bitmap, next, shape, nx, ny)
    elif (x, y) in shape['corners']:
        return shape
    else:
        next = direction(bitmap, x, y)
        shape['corners'].append((x, y))
        shape = trace(bitmap, next, shape, x, y)

    return shape


def erase(bitmap, points):
    for x, y in points:
        print(x, y)
        bitmap[x][y] = '0'


def main():
    bitmap = get_input()
    draw(bitmap)
    shapes = []

    while True:
        shape_at = find(bitmap)

        s = {
            'corners': [shape_at],
            'points': []
        }

        shape = trace(bitmap, direction(bitmap, *shape_at), s, *shape_at)

        if not shape:
            break

        shapes.append(shape)
        import pprint
        pprint.pprint(shapes)
        draw(bitmap)


if __name__ == '__main__':
    main()
