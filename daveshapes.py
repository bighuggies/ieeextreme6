import sys


def poss_poses(r, c, rows, cols):
    poses = []

    if (r + 1) <= rows:
        poses.append((1, 0))
    if (r + 1) <= rows and (c + 1) <= cols:
        poses.append((1, 1))
    if (c + 1) <= cols:
        poses.append((0, 1))
    if (r + 1) <= rows and (c - 1) >= 0:
        poses.append((1, -1))
    if (c - 1) >= 0:
        poses.append((0, -1))
    if (r - 1) >= 0:
        poses.append((-1, 0))
    if (r - 1) >= 0 and (c + 1) <= cols:
        poses.append((-1, 1))
    if (r - 1) >= 0 and (c - 1) >= 0:
        poses.append((-1, -1))

    return poses


def get_shape(verts):
    if len(verts) == 4:
        return "Triangle"

    center = verts[1]
    above = verts[0]
    right = verts[2]

    if (above[0] == center[0] or above[1] == center[1]) and (right[0] == center[0] or right[1] == center[1]):
        l1 = max(abs(above[0] - center[0]), abs(above[1] - center[1]))
        l2 = max(abs(right[0] - center[0]), abs(right[1] - center[1]))
        if l1 == l2:
            return "Square"
        else:
            return "Rectangle"
    else:
        return "Parallelogram"


def find_shape(grid):

    rows, cols = len(grid), len(grid[0])

    flag = False
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                flag = True
                break
        if flag:
            break

    curr = (r, c)
    verts = []
    verts.append(curr)
    pixels = []

    #print curr

    first = True
    while True:
        if len(verts) > 2 and verts[0] == verts[-1]:
            break

        poss = poss_poses(curr[0], curr[1], rows, cols)
        for p in poss:
            try:
                if grid[curr[0] + p[0]][curr[1] + p[1]] == 1:
                    direction = p
                    break
            except:
                pass

        if first:
            curr = (curr[0] + p[0], curr[1] + p[1])
            grid[curr[0]][curr[1]] = 0
            first = False
        try:
            while grid[curr[0] + p[0]][curr[1] + p[1]] == 1:
                grid[curr[0]][curr[1]] = 0
                curr = (curr[0] + p[0], curr[1] + p[1])
        except:
            pass

        grid[curr[0]][curr[1]] = 0

        verts.append(curr)
        #print verts

    return get_shape(verts), grid


def solve(grid):
    s = []
    finished = False
    while not finished:
        bits = []
        for x in grid:
            bits.extend(x)
        if 1 not in bits:
            finished = True
        else:
            shape, grid = find_shape(grid)
            s.append(shape)

    s.sort()
    #print 'Here'
    print ', '.join(s)


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
            bitmap[x].append(int(bitstring[x * int(columns) + y]))

    return bitmap


if __name__ == '__main__':
    grid = get_input()

    import pprint; pprint.pprint(grid)

    solve(grid)
