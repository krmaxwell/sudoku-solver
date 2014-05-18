import sys


class Puzzle(object):

    def __init__(self, grid):
        self.cells = dict()
        for x in xrange(9):
            for y in xrange(9):
                self.cells['value'][x][y] = grid[x][y]

    def __repr__(self):
        for x in xrange(9):
            for y in xrange(9):
                print self.cells['value'][x][y],
            print 'n'

    def solve(self):
        pass

def main():
    with open(sys.argv[1], 'rb') as f:
        raw_data = f.readlines()

    data = []
    for line in raw_data:
        row = []
        for d in line.rstrip('\n'):
            row.append(int(d))
        data.append(row)

    puzzle = Puzzle(data)
    print "Initial state: %r" % puzzle
    puzzle.solve()


if __name__ == "__main__":
    main()