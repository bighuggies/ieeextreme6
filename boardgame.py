#!/usr/bin/env python


def parse():
    line = raw_input()
    sizedem, places = line.split(':')
    size, dimensions = sizedem.split('-')

    print(p)
    p = [s.strip('{}$').split() for s in places.split('}{')]


    return(size, dimensions, p)


def main():
    size, dimensions, positions = parse()

    print(positions)


if __name__ == '__main__':
    main()
